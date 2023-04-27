from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myadmin import models
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request, 'myhome/index.html')


def login(request):
    return render(request, 'myhome/login/login.html')


def dologin(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    obj = models.Users.objects.filter()
    num = models.Users.objects.filter().count()
    if not num:
        return HttpResponse('<script>alert("用户不存在");history.back()</script>')
    else:
        if check_password(data['password'], obj[0].password):
            request.session['VipUser'] = {'phone': obj[0].phone, 'id': obj[0].id}
            return HttpResponse('<script>alert("登录成功");location.href="/"</script>')
        else:
            return HttpResponse('<script>alert("登录失败");history.back()</script>')

def logout(request):
    request.session.flush()
    return HttpResponse('<script>alert("退出成功");location.href="/myhome/login"</script>')

def register(request):
    return render(request, 'myhome/register/register.html')


def doregister(request):
    return HttpResponse('注册页面')


def checkphone(request):
    data = request.GET.get('phone')

    count = models.Users.objects.filter(phone=data).count()
    if count:
        return JsonResponse({'code': 0, 'msg': '手机号已存在'})
    else:
        return JsonResponse({'code': 1, 'msg': '手机号可以使用'})


def sendcode(request):
    phone = request.GET.get('phone')
    if phone:
        return JsonResponse({'code': 0, 'msg': '验证码已发送', 'vcode': '123456'})
