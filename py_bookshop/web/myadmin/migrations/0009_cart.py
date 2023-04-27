# Generated by Django 3.2.8 on 2021-10-30 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_alter_bookimgs_img_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('select', models.IntegerField(default=0)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.books')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.users')),
            ],
        ),
    ]
