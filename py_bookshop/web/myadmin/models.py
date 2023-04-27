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


class BookType(models.Model):
    name = models.CharField(max_length=50)
    pid = models.IntegerField()
    path = models.CharField(max_length=50)


class Books(models.Model):
    typeid = models.ManyToManyField(to="BookType")
    title = models.CharField(max_length=100)
    tuijian = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    price = models.FloatField()
    num = models.IntegerField()
    ISBN = models.CharField(max_length=100)
    context = models.TextField()


class BookImgs(models.Model):
    bookid = models.ForeignKey('Books', on_delete=models.CASCADE)
    img_url = models.ImageField(upload_to='static/uploads/')


class Cart(models.Model):
    uid = models.ForeignKey('Users', on_delete=models.CASCADE)
    bid = models.ForeignKey('Books', on_delete=models.CASCADE)
    num = models.IntegerField()
    select = models.IntegerField(default=0)


class Order(models.Model):
    uid = models.ForeignKey('Users', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)

    totalprice = models.FloatField()
    status = models.IntegerField(default=0)
    ordertime = models.DateTimeField(auto_now_add=True)
    paytime = models.DateTimeField(null=True)


class OrderDetail(models.Model):
    orderid = models.ForeignKey('Order', on_delete=models.CASCADE)
    bid = models.ForeignKey('Books', on_delete=models.CASCADE)
    num = models.IntegerField()
    price = models.FloatField()
