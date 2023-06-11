from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','tipo','descripcion','vencimiento','imagen',]
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['tipo']
    list_editable = ['precio','stock','tipo','descripcion','vencimiento','imagen']


admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)

