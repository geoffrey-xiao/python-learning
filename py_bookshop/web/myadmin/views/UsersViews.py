from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from ..models import Users
import random
import time
import os


def index(request):
    data = Users.objects.filter()
    selecttype = request.GET.get('selecttype', None)
    keywords = request.GET.get('keywords', None)
    print(selecttype, keywords)
    if selecttype:
        if selecttype == 'all':
            from django.db.models import Q
            data = data.filter(Q(nickname__contains=keywords)|Q(homeaddress__contains=keywords))
        else:
            selectdata = {f'{selecttype}__contains': keywords}
            data = data.filter(**selectdata)
    context = {'data': data}
    return render(request, 'myadmin/users.html', context)


def add(request):
    id = request.GET.get('id')
    if id:
        data = Users.objects.get(id=id)
        print(data)
        context = {'data': data}
        return render(request, 'myadmin/usersadd.html', context)
    else:
        return render(request, 'myadmin/usersadd.html')


def insert(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    file = request.FILES.get('avatar')
    if file:
        data['avatar'] = imageupload(file)
    else:
        if data['id']:
            data['avatar'] = data['old_avatar']
        else:
            data.pop('avatar')
    data.pop('old_avatar')

    data['password'] = make_password(data['password'], None, 'pbkdf2_sha256')
    print(data)
    if data['id']:
        Users.objects.filter(id=data['id']).update(**data)
        url = reverse('myadmin_users')
        return HttpResponse(f'<script>alert("更新用户成功");location.href="{url}"</script>')
    else:
        try:
            data.pop('id')
            obj = Users(**data)
            obj.save()
            print(obj)
            url = reverse('myadmin_users')
            return HttpResponse(f'<script>alert("添加用户成功");location.href="{url}"</script>')
        except:
            url = reverse('myadmin_users_add')
            return HttpResponse(f'<script>alert("添加用户失败");location.href="{url}"</script>')


def delete(request):
    try:
        id = request.GET.get('id')
        data = Users.objects.get(id=id)
        print(id)
        try:
            if 'uploads' in data.avatar:
                os.remove('.'+data.avatar)
        except:
            return JsonResponse({'code': 2, 'msg': '删除头像失败'})
        data.delete()
        return JsonResponse({'code': 0, 'msg': '删除成功'})
    except:
        return JsonResponse({'code': 1, 'msg': '删除失败'})


def edit(request):
    id = request.GET.get('id')
    data = Users.objects.get(id=id)
    context = {'data': data}
    return render(request, 'myadmin/usersadd.html', context)


def imageupload(file):
    filename = str(random.randint(1000, 9999) + time.time()) + \
        '.'+file.name.split('.').pop()
    with open(f'./static/uploads/{filename}', 'wb+') as fp:
        fp.write(file.read())
    return f'/static/uploads/{filename}'
