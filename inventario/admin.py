from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'total_productos')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

    def total_productos(self, obj):
        return obj.productos.count()
    total_productos.short_description = "Cant. Productos"


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'existencias', 'fecha_registro')
    list_filter = ('categoria', 'fecha_registro')
    search_fields = ('nombre', 'descripcion', 'categoria__nombre')
    list_editable = ('precio', 'existencias')
    ordering = ('-fecha_registro',)
    date_hierarchy = 'fecha_registro'
