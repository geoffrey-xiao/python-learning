from django.shortcuts import render, reverse

from django.http import HttpResponse

from . import models

import os
# Create your views here.


def index(request):
    return HttpResponse('hello world')


def love(request):
    # return HttpResponse('iloveyou')
    return render(request, 'a/ind.html')


def modelTest(request):
    # 添加数据

    # data = {
    #     'name': '隔壁老王',
    #     'age': 30,
    #     'sex': '1',
    #     'address': '西安...'
    # }
    # obj = models.Stu(**data)
    # obj.save()

    # 查询数据

    # data = models.Stu.objects.all()
    # print(data)
    # for i in data:
    #   print(i.name)

    # 删除数据
    # models.Stu.objects.filter(id = 4).delete()

    # 修改数据
    # models.Stu.objects.filter(name="隔壁老王").update(address="郑州")
    obj = models.Stu.objects.get(name="隔壁老王")
    obj.name = "隔壁老刘"
    obj.save()
    return HttpResponse('模型测试')


def modelRelation(request):
    # 一对一关系
    # 创建模型
    # stuobj = {
    #     'name': 'summer',
    #     'age': 4,
    #     'sex': '0',
    #     'address': '家里蹲'
    # }
    # obj = models.Student(**stuobj)
    # obj.save()

    # infoobj = {
    #     'sid': obj,
    #     'xueli': '小学',
    #     'phone': '123456766'
    # }
    # info = models.StuInfo(**infoobj)
    # info.save()

    # 查询数据
    # obj = models.Student.objects.last()
    # print(obj.name)
    # print(obj.stuinfo.xueli)

    # obj = models.StuInfo.objects.last()
    # print(obj.xueli)
    # print(obj.sid.name)

    # 删除数据
    # obj = models.Student.objects.last()
    # obj.delete()

    # 一对多关系
    # obj = models.Banji(bname='1班')
    # obj.save()
    # s1 = {
    #     'name': 'summer',
    #     'age': 4,
    #     'sex': '0',
    #     'address': '家里蹲',
    #     'bid': obj
    # }
    # s2 = {
    #     'name': 'zhangsan',
    #     'age': 20,
    #     'sex': '0',
    #     'address': '北京',
    #     'bid': obj
    # }
    # obj1 = models.Student(**s1)
    # obj2 = models.Student(**s2)
    # obj1.save()
    # obj2.save()

    # 查询
    # bobj = models.Banji.objects.first()
    # print(bobj.bname)
    # print(bobj.student_set.all())
    # stus = bobj.student_set.all()
    # for i in stus:
    #     print(i.name)

    models.Banji.objects.get(id=1).delete()
    return HttpResponse('模型关系')


def addbook(request):
    return render(request, 'book/addbook.html')


def insertbook(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    print(data)
    file = uploadimg(request)
    if file:
        data['img_url'] = file
        obj = models.Books(**data)
        obj.save()
        url = reverse('booklist')
        return HttpResponse('<script>alert("添加成功");location.href="'+url+'"</script>')


def uploadimg(request):
    file = request.FILES['img_url']
    import random
    import time
    zh = file.name.split('.').pop()
    name = str(random.randint(1000, 9999) + time.time()) + '.' + zh
    with open(f'./static/uploads/{name}', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    filename = f'/static/uploads/{name}'
    return filename


def querybook(request):
    data = models.Books.objects.all()
    print(data)
    context = {'data': data}
    return render(request, 'book/index.html', context)


def delbook(request, id):
    try:
        obj = models.Books.objects.get(id=id)
        os.remove('.' + obj.img_url)
        obj.delete()
        info = '删除成功'
    except:
        info = '删除失败'
    url = reverse('booklist')
    return HttpResponse(f'<script>alert("{info}");location.href="{url}"</script>')


def editbook(request):
    id = request.GET.get('id')
    obj = models.Books.objects.get(id=id)
    return render(request, 'book/editbook.html', {'obj': obj})


def updatebook(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    print(data)
    file = request.FILES.get('img_url', None)
    print(file)
    if(file):
        print('有图片')
        filename = uploadimg(request)
        # os.remove('.'+data['old_img_url'])
        data['img_url'] = filename
        print(data['old_img_url'])
    else:
        print('无图片')
        data['img_url'] = data['old_img_url']
    data.pop('old_img_url')
    try:
        models.Books.objects.filter(id=data['id']).update(**data)
        url = reverse('booklist')
        return HttpResponse(f'<script>alert("更新成功");location.href="{url}"</script>')
    except:
        url = reverse('editbook')
        return HttpResponse(f'<script>alert("更新失败");location.href="{url}?id={data["id"]}"</script>')
