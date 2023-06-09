# Generated by Django 3.2.8 on 2021-10-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0002_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=80)),
                ('avatar', models.CharField(default='/static/myadmin/assets/img/user03.png', max_length=100, null=True)),
                ('homeaddress', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=50, null=True)),
                ('sex', models.CharField(max_length=20, null=True)),
                ('usertype', models.CharField(max_length=20, null=True)),
                ('registertime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
