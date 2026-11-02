from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls')),
]

admin.site.site_header = "Catálogo de Productos - Administración"
admin.site.site_title = "Admin Catálogo"
admin.site.index_title = "Panel de Gestión de Inventario"
