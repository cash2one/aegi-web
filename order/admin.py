from django.contrib import admin
from order.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#for submitModel app
class submitModelResource(resources.ModelResource):
    class Meta:
        model = orderModel

# Register your models here.
class orderModelAdmin(ImportExportModelAdmin):
    list_display = ('number', 'haveKit','kitId','username','email','phone','province','city','county','address','paymentMethod','radioInvoice','invoice','message')
    list_filter = ['haveKit','province','city','paymentMethod']
    search_fields = ['kitId','username','email','phone','invoice','message']
    change_list_template = 'smuggler/change_list.html'
    resource_class = submitModelResource
    pass

# register the admin class
admin.site.register(orderModel,orderModelAdmin)