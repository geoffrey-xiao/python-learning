from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', views.index, name="myadmin"),

    path('', IndexViews.index, name="myadmin"),

    path('login/', IndexViews.login, name="myadmin_login"),
    path('gologin/', IndexViews.gologin, name="myadmin_gologin"),

    path('checkcode/', IndexViews.verifycode, name="myadmin_check_code"),

    path('users/index', UsersViews.index, name="myadmin_users"),

    path('users/add', UsersViews.add, name="myadmin_users_add"),

    path('users/insert', UsersViews.insert, name="myadmin_users_insert"),

    path('users/delete', UsersViews.delete, name="myadmin_users_delete"),

    # path('users/add', UsersViews.edit, name="myadmin_users_add"),

    path('types/index', TypesViews.index, name="myadmin_types"),

    path('types/add', TypesViews.add, name="myadmin_types_add"),

    path('types/insert', TypesViews.insert, name="myadmin_types_insert"),

    path('types/delete', TypesViews.delete, name="myadmin_types_delete"),

    path('types/edit', TypesViews.edit, name="myadmin_types_edit"),

    path('books/index', BooksViews.index, name="myadmin_books"),

    path('books/add', BooksViews.add, name="myadmin_books_add"),

    path('books/insert', BooksViews.insert, name="myadmin_books_insert"),

    path('books/delete', BooksViews.delete, name="myadmin_books_delete"),

    path('orders/index', OrdersViews.index, name="myadmin_orders"),
]
