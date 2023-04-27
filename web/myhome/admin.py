from django.contrib import admin

# Register your models here.

from .import models


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'price', 'publisher', 'pub_date',)

    ordering = ('id',)

    list_editable = ['name','author','publisher']

    list_per_page = 10

    search_fields = ('name','author','publisher')

    list_filter = ('name','author','publisher','pub_date')

    date_hierarchy = 'pub_date'


admin.site.register(models.Books, BookAdmin)
