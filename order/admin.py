from django.contrib import admin
from order.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
class orderModelResource(resources.ModelResource):
    class Meta:
        model = orderModel

# Register your models here.
class orderModelAdmin(ImportExportModelAdmin):
    list_display = ('number', 'haveKit','kitId','username','email','phone','province','city','county','address','paymentMethod','radioInvoice','invoice','message')
    list_filter = ['haveKit','province','city','paymentMethod']
    search_fields = ['kitId','username','email','phone','invoice','message']
    change_list_template = 'smuggler/change_list.html'
    resource_class = orderModelResource
    pass


class productModelResource(resources.ModelResource):
    class Meta:
        model = productModel

# Register your models here.
class productModelAdmin(ImportExportModelAdmin):
    list_display = ('kitId','price')
    list_filter = ['price']
    search_fields = ['kitId']
    change_list_template = 'smuggler/change_list.html'
    resource_class = productModelResource
    pass

# register the admin class
admin.site.register(orderModel,orderModelAdmin)
admin.site.register(productModel,productModelAdmin)
