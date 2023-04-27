# Generated by Django 3.2.8 on 2021-10-13 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0005_auto_20211013_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(default='0', max_length=1)),
                ('address', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StuInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xueli', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('sid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myhome.student')),
            ],
        ),
    ]
