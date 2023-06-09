# Generated by Django 3.2.8 on 2021-10-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=80)),
                ('avatar', models.CharField(max_length=100, null=True)),
                ('homeaddress', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=50, null=True)),
                ('sex', models.CharField(max_length=1, null=True)),
                ('usertype', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
