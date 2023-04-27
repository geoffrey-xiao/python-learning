from django.urls import path, include
from .views import *

urlpatterns = [
    # 首页
    path('', IndexViews.index, name="myhome"),
    path('booklist/<int:pid>/<int:cid>',
         IndexViews.booklist, name="myhome_booklist"),
    path('detail', IndexViews.detail, name="myhome_detail"),

    # 购物车
    path('cart', CartViews.index, name="myhome_cart_index"),
    path('addcart', CartViews.addcart, name="myhome_cart_add"),
    path('editcart', CartViews.editcart, name="myhome_cart_edit"),
    path('deletecart', CartViews.deletecart, name="myhome_cart_delete"),
    path('viewcart', CartViews.cartinfo, name="myhome_cart_view"),

    # 订单页
    path('order', OrderViews.index, name="myhome_order_index"),
    path('createorder', OrderViews.create, name="myhome_order_create"),
    path('gopay/<int:oid>', OrderViews.gopay, name="myhome_order_gopay"),
    path('myorder', OrderViews.myorder, name="myhome_order_myorder"),

    # 登录
    path('myhome/login', LoginViews.login, name="myhome_login"),
    path('myhome/dologin', LoginViews.dologin, name="myhome_dologin"),
    path('myhome/logout', LoginViews.logout, name="myhome_logout"),
    path('myhome/register', LoginViews.register, name="myhome_register"),
    path('myhome/doregister', LoginViews.doregister, name="myhome_doregister"),
    path('myhome/checkphone', LoginViews.checkphone, name="myhome_checkphone"),
    path('myhome/sendcode', LoginViews.sendcode, name="myhome_sendcode"),
]
