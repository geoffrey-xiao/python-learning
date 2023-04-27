from django.shortcuts import render, reverse
from django.http import HttpResponse
# Create your views here.
from .. import models


def queryTypes():
	data = models.BookType.objects.extra(
		select={'paths': 'concat(path,id)'}).order_by('paths')
	for i in data:
		num = i.path.count(',')-1
		i.sb = '|----' * num
		if i.pid != 0:
			i.pname = models.BookType.objects.get(id=i.pid).name
	return data


def index(request):
	data = models.Books.objects.filter()
	selecttype = request.GET.get('selecttype')
	keywords = request.GET.get('keywords')
	if selecttype:
		if selecttype == 'all':
			from django.db.models import Q
			data = data.filter(Q(title__contains=keywords) |
							   Q(author__contains=keywords))
		else:
			selectdata = {f'{selecttype}__contains': keywords}
			data = data.filter(**selectdata)

	context = {'data': data}
	return render(request, 'myadmin/books/index.html', context)


def add(request):
	data = queryTypes()
	context = {'data': data}
	return render(request, 'myadmin/books/add.html', context)


def insert(request):
	data = request.POST.dict()
	typeid = request.POST.getlist('typeid')
	typeobj = models.BookType.objects.filter(id__in=typeid)
	print(typeobj)
	data.pop('csrfmiddlewaretoken')
	print(data)
	file = request.FILES.get('pic', None)
	if not file:
		return HttpResponse('<script>alert("请选择一张图书封面图");history.back()</script>')
	data.pop('typeid')
	try:
		obj = models.Books(**data)
		obj.save()
		obj.typeid.set(typeobj)
		img_obj = models.BookImgs()
		img_obj.bookid = obj
		img_obj.img_url = file
		img_obj.save()
		url = reverse('myadmin_books')
		return HttpResponse(f'<script>alert("添加图书成功");location.href="{url}"</script>')
	except:
		url = reverse('myadmin_books_add')
		return HttpResponse(f'<script>alert("添加图书失败");location.href="{url}"</script>')


def delete(request):
	pass
