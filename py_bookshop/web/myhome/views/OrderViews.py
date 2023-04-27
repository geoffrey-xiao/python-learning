from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, JsonResponse
from myadmin import models
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from myadmin import models
from .IndexViews import getcategory


def index(request):
    ids = request.GET.get('ids').split(',')
    data = models.Cart.objects.filter(id__in=ids)
    context = {'booktype': getcategory(), 'carts': data}
    return render(request, 'myhome/checkout/checkout.html', context)


def create(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    vipuser = request.session['VipUser']
    totalprice = 0
    ids = data['ids'].split(',')
    carts = models.Cart.objects.filter(id__in=ids)
    for i in carts:
        totalprice += i.num * i.bid.price

    orderdata = {
        'uid': models.Users.objects.get(id=vipuser['id']),
        'name': data['name'],
        'phone': data['phone'],
        'address': data['address'],
        'totalprice': float("%.2f" % totalprice)
    }
    orderobj = models.Order(**orderdata)
    orderobj.save()

    for i in carts:
        detaildata = {
            'orderid': orderobj,
            'bid': i.bid,
            'num': i.num,
            'price': i.bid.price
        }
        detailobj = models.OrderDetail(**detaildata)
        detailobj.save()
        i.delete()
    print(data)
    url = reverse('myhome_order_gopay', args=(orderobj.id,))
    return redirect(url)


def gopay(request, oid):
    print(oid)
    return HttpResponse('去支付')


def myorder(request):
    user = request.session['VipUser']
    if not user['id']:
        return HttpResponse('<script>alert("请先登录");location.href="/myhome/login"</script>')
    else:
        user = models.Users.objects.get(id=user['id'])
        context = {'booktype': getcategory(), 'user': user}
        return render(request, 'myhome/myorder/myorder.html', context)
