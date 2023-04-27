from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', views.index, name="myadmin"),

    path('', IndexViews.index, name="myadmin"),

    path('users/index', UsersViews.index, name="myadmin_users"),

    path('users/add', UsersViews.add, name="myadmin_users_add"),

    path('users/insert', UsersViews.insert, name="myadmin_users_insert"),

    path('users/delete', UsersViews.delete, name="myadmin_users_delete"),

    path('types/index', TypesViews.index, name="myadmin_types"),

    path('books/index', BooksViews.index, name="myadmin_books"),

    path('orders/index', OrdersViews.index, name="myadmin_orders"),
]
