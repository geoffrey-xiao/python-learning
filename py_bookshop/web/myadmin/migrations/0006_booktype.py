# Generated by Django 3.2.8 on 2021-10-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_alter_users_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pid', models.IntegerField()),
                ('path', models.CharField(max_length=50)),
            ],
        ),
    ]