from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myadmin import models
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from myadmin import models
from .IndexViews import getcategory
from django.core import serializers

def cartinfo(request):
    user = request.session['VipUser']
    if not user['id']:
        return JsonResponse({'code':1,'msg':'请先登录'})
    else:
        data = models.Users.objects.get(id=user['id'])
        carts = data.cart_set.all()
        arr = []
        for i in carts:
            obj = {
                'num':i.num,
                'price':i.bid.price,
                'title':i.bid.title,
            }
            arr.append(obj)
        print(arr)

        # cartlist = 
    return JsonResponse({'code':1,'data':arr})

def index(request):
    user = request.session['VipUser']
    if not user['id']:
        return JsonResponse({'code':1,'msg':'请先登录'})
    else:
        data = models.Users.objects.get(id=user['id'])
    context = {'booktype': getcategory(),'data':data}
    return render(request, 'myhome/cart/cart.html', context)

def addcart(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    user = request.session['VipUser']
    if not user['id']:
        return JsonResponse({'code':1,'msg':'请先登录'})
    else:
        data['uid']= models.Users.objects.get(id=user['id'])
        data['bid']=models.Books.objects.get(id=data['bid'])
        print(data)
        try:
            cart = data['uid'].cart_set.filter(bid=data['bid'])
            if cart.count():
                obj = cart[0]
                obj.num += int(data['num'])
                obj.save()
            else:
                obj = models.Cart(**data)
                obj.save()
            return JsonResponse({'code':0,'msg':'加入购物车成功'})
        except:
            return JsonResponse({'code':1,'msg':'加入购物车失败'})

def editcart(request):
    cid = request.GET.get('cid')
    num = request.GET.get('n')
    print(cid)
    try:
        obj = models.Cart.objects.get(id=cid)
        obj.num=num
        obj.save()
        return JsonResponse({'code':0,'msg':'更新购物车成功'})
    except:
        return JsonResponse({'code':1,'msg':'更新购物车失败'})

def deletecart(request):
    cid = request.GET.get('cid')
    print(cid)
    try:
        obj = models.Cart.objects.get(id=cid)
        obj.delete()
        return JsonResponse({'code':0,'msg':'删除购物车成功'})
    except:
        return JsonResponse({'code':1,'msg':'删除购物车失败'})

