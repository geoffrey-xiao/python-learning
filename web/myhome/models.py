from django.db import models

# Create your models here.


class Stu(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, default='0')
    address = models.CharField(max_length=50, null=True)


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, default='0')
    address = models.CharField(max_length=50, null=True)

    bid = models.ForeignKey(to="Banji", on_delete=models.CASCADE)


class StuInfo(models.Model):
    sid = models.OneToOneField(Student, on_delete=models.CASCADE)
    xueli = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)


class Banji(models.Model):
    bname = models.CharField(max_length=20)


# class Teacher(models.Model):
#     tname = models.CharField(max_length=20)
#     tid = models.ManyToManyField(to="Banji")


class Books(models.Model):
    name = models.CharField(max_length=50)

    author = models.CharField(max_length=100)

    publisher = models.CharField(max_length=50)

    price = models.FloatField()

    introduction = models.TextField()

    img_url = models.CharField(max_length=50, null=True)

    pub_date = models.DateField()
