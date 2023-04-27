from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.love),

    path('model', views.modelTest, name="mymodel"),

    path('modelrelation',views.modelRelation,name="modelRelation"),

    path('addbook', views.addbook, name="addbook"),

    path('insertbook', views.insertbook, name="insertbook"),

    path('booklist', views.querybook, name="booklist"),

    path('delbook/<int:id>', views.delbook, name="delbook"),

    path('editbook', views.editbook, name="editbook"),

    path('updatebook', views.updatebook, name="updatebook")
]
