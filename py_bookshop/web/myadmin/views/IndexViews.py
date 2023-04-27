import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.
from .. import models
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request, 'myadmin/index.html')


def login(request):
    return render(request, 'myadmin/login.html')


def gologin(request):
    data = request.POST.dict()
    print(data)
    obj = models.Users.objects.filter(phone=data['phone'])
    if request.session['verify'].lower() != data['checkcode'].lower():
        return HttpResponse('<script>alert("验证码不正确");history.back()</script>')
    if obj.count() == 0:
        return HttpResponse('<script>alert("用户不存在");history.back()</script>')
    if check_password(data['password'], obj[0].password):
        request.session['AdminUser'] = {'id': obj[0].id, 'phone': obj[0].phone}
        url = reverse('myadmin')
        return HttpResponse(f'<script>alert("登陆成功");location.href="{url}"</script>')
    else:
        return HttpResponse('<script>alert("密码错误");history.back()</script>')


def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    from io import BytesIO
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(20, 100))
    width = 100
    height = 30
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象,按照目录找自己电脑的字体，关于后缀，otf或者TTF
    font = ImageFont.truetype('Arial.ttf', 24)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verify'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'img/png')
