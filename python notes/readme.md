## 创建项目

django-admin startproject web



## 启动项目 进入到项目目录中，在manage.py文件的同级目录中，执行命令

python manage.py runserver



## 目录结构

```
web
├── db.sqlite3
├── manage.py
└── web
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   ├── settings.cpython-39.pyc
    │   ├── urls.cpython-39.pyc
    │   └── wsgi.cpython-39.pyc
    ├── asgi.py
    ├── settings.py  #配置文件
    ├── urls.py      #路由文件
    └── wsgi.py。    #网关文件

```

## 创建web应用

`python manage.py startapp myhome`



## 给视图函数创建路由

```python
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index)
]
```



## 在根路由中配置当前应用的路径

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myhome.urls'))
]
```

## 在项目中使用模版

````python
# 修改settings.py模版引擎的配置目录 settings.py/Templates/DIRS
'DIRS':[os.path.join(BASE_DIRS),'templates']
  
#1.在manage.py 文件同级目录下，创建templates文件夹
#2.在模版文件夹中创建模版文件 .html文件
#3.在视图函数中使用模版文件 myhome/views.py
```
def func(request):
  return render(request,'a/ind.html')
```
````



## 在项目中使用静态文件(css,js,img...)

```python
# 修改settings.py模版引擎的配置目录 settings.py/Templates/DIRS

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
# 1.在manage.py同级目录下创建static文件夹
# 2.在静态文件夹中创建静态文件

```

 当前的项目目录结构

```python
./WEB                    --项目目录
├── db.sqlite3					 --django默认的数据库配置，生成的数据库文件
├── manage.py						 --管理文件，当前项目唯一的入口文件
├── myhome               --自定义创建的应用
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py       --当前应用中的模型文件
│   ├── tests.py
│   ├── urls.py          --当前应用中的路由文件
│   └── views.py         --当前应用中的视图函数
├── static               --静态文件夹
│   ├── 1.css
│   └── ind.css
├── templates            --模版文件夹
│   └── a
│       └── ind.html
└── web
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


```

## 模型的配置和定义

```python
#1.在setting.py中修改数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# 2.添加自定义应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myhome'
]

#3.在应用中的models.py中定义模型
from django.db import models
class Stu(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	sex = models.CharField(max_length=1,default='0')
	address = models.CharField(max_length=50,null=True) 
 #4.生成迁移文件
python3 manage.py makemigrations

#5.执行迁移文件
python3 manage.py migrate

```



## 模型的使用

```python
 # 添加数据

    data = {
        'name': '隔壁老王',
        'age': 30,
        'sex': '1',
        'address': '西安...'
    }
    obj = models.Stu(**data)
    obj.save()

    # 查询数据

     data = models.Stu.objects.all()
     print(data)
     for i in data:
     	print(i.name)

    # 删除数据
     models.Stu.objects.filter(id = 4).delete()

    # 修改数据
     models.Stu.objects.filter(name="隔壁老王").update(address="郑州")
    obj = models.Stu.objects.get(name="隔壁老王")
    obj.name = "隔壁老刘"
    obj.save()
```

