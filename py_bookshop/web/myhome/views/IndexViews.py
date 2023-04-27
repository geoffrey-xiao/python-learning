from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myadmin import models
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from myadmin import models


def index(request):
    books = models.Books.objects.filter()
    context = {'booktype': getcategory(), 'books': books}
    return render(request, 'myhome/index.html', context)


def booklist(request, pid, cid):
    data = models.BookType.objects.get(id=pid)
    data.cate = models.BookType.objects.filter(pid=pid)
    if cid == 0:
        data.sub = models.BookType.objects.filter(pid=pid)
    else:
        data.sub = models.BookType.objects.filter(id=cid)
        data.cname = models.BookType.objects.get(id=cid).name
    print(data)
    context = {'booktype': getcategory(), 'data': data,'cid':cid}
    return render(request, 'myhome/booklist/shop.html', context)


def detail(request):
    bid = request.GET.get('id')
    data = models.Books.objects.get(id=bid)
    context = {'booktype': getcategory(),'data':data}
    return render(request, 'myhome/detail/detail.html', context)


def getcategory():
    data = models.BookType.objects.filter(pid=0)
    for i in data:
        i.sub = models.BookType.objects.filter(pid=i.id)
    return data
