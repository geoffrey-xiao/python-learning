from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .. import models


def queryTypes():
    data = models.BookType.objects.extra(
        select={'paths': 'concat(path,id)'}).order_by('paths')
    for i in data:
        num = i.path.count(',')-1
        i.sb = '|----' * num
        if i.pid != 0:
            i.pname = models.BookType.objects.get(id=i.pid).name
    return data


def index(request):
    data = queryTypes()
    context = {'data': data}
    return render(request, 'myadmin/types/index.html', context)


def add(request):
    data = queryTypes()
    context = {'data': data}
    return render(request, 'myadmin/types/add.html', context)


def insert(request):
    data = request.POST.dict()
    print(data)
    data.pop('csrfmiddlewaretoken')
    if data['pid'] == '0':
        data['path'] = '0,'
    else:
        path = models.BookType.objects.get(id=data['pid']).path
        data['path'] = path+data['pid']+','
    try:
        obj = models.BookType(**data)
        obj.save()
        url = reverse('myadmin_types')
        return HttpResponse(f'<script>alert("添加分类成功");location.href="{url}"</script>')
    except:
        url = reverse('myadmin_types_add')
        return HttpResponse(f'<script>alert("添加分类失败");location.href="{url}"</script>')


def delete(request):
    id = request.GET.get('id')

    num = models.BookType.objects.filter(pid=id).count()
    print(num)
    if num:
        return JsonResponse({'code': 1, 'msg': '当前分类下有子类，不能删除'})
    obj = models.BookType.objects.get(id=id)
    obj.delete()
    return JsonResponse({'code': 0, 'msg': '删除成功'})


def edit(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    try:
        obj = models.BookType.objects.get(id=id)
        obj.name = name
        obj.save()
        return JsonResponse({'code':0,'msg':'更新成功'})
    except:
        return JsonResponse({'code':1,'msg':'更新失败'})
