from django.db import models

# Create your models here.


class Users(models.Model):
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=200)
    avatar = models.CharField(
        max_length=100, default="/static/myadmin/assets/img/user03.png")

    homeaddress = models.CharField(max_length=100, null=True)

    nickname = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=20, null=True)
    usertype = models.CharField(max_length=20, null=True)

    registertime = models.DateTimeField(auto_now_add=True)
