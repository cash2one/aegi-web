from django.contrib import admin
from models import news
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django import forms
from django.db import models

class newsResource(resources.ModelResource):
    class Meta:
        model = news

class newsAdmin(ImportExportModelAdmin):
    list_display = ('newsId','title', 'abstract','author','time','content')
    list_filter = ['time','author']
    search_fields = ['title','abstract','content']
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    class Media:
        js = ('/static/ckeditor/ckeditor.js',)

    change_list_template = 'smuggler/change_list.html'

    resource_class = newsResource
    pass

# register the admin class
admin.site.register(news,newsAdmin)