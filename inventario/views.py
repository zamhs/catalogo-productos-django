from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Sum, Avg, F, DecimalField
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm


def lista_productos(request):
    """
    Fase 6: Consultar productos
    Fase 7: Implementar búsqueda con icontains
    Fase 8: Ordenamiento con order_by
    Fase 9: Estadísticas con Count(), Sum(), Avg()
    """
    productos = Producto.objects.select_related('categoria').all()

    # Filtro de búsqueda por nombre (icontains)
    texto_busqueda = request.GET.get('buscar', '').strip()
    if texto_busqueda:
        productos = productos.filter(nombre__icontains=texto_busqueda)

    # Filtro por categoría
    categoria_id = request.GET.get('categoria', '')
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # Ordenamiento
    criterio_orden = request.GET.get('orden', '-fecha_registro')
    ordenes_validos = {
        'nombre': 'nombre',
        '-nombre': '-nombre',
        'precio': 'precio',
        '-precio': '-precio',
        'existencias': 'existencias',
        '-existencias': '-existencias',
        'fecha': 'fecha_registro',
        '-fecha_registro': '-fecha_registro'
    }
    campo_orden = ordenes_validos.get(criterio_orden, '-fecha_registro')
    productos = productos.order_by(campo_orden)

    # Fase 9: Estadísticas del Catálogo e Inventario
    # Calculamos sobre todos los productos para mostrar el estado general del negocio
    stats_base = Producto.objects.all()
    total_productos = stats_base.count()
    total_existencias = stats_base.aggregate(total=Sum('existencias'))['total'] or 0
    precio_promedio = stats_base.aggregate(prom=Avg('precio'))['prom'] or 0
    
    # Valor total del inventario: Sum(precio * existencias)
    valor_inventario = stats_base.aggregate(
        total=Sum(F('precio') * F('existencias'), output_field=DecimalField())
    )['total'] or 0

    categorias = Categoria.objects.all()

    context = {
        'productos': productos,
        'categorias': categorias,
        'texto_busqueda': texto_busqueda,
        'categoria_seleccionada': categoria_id,
        'orden_seleccionado': criterio_orden,
        'total_productos': total_productos,
        'total_existencias': total_existencias,
        'precio_promedio': precio_promedio,
        'valor_inventario': valor_inventario,
    }
    return render(request, 'inventario/lista_productos.html', context)


def crear_producto(request):
    """
    Fase 6: Crear producto en /productos/nuevo/
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'¡El producto "{producto.nombre}" fue registrado exitosamente!')
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'inventario/formulario_producto.html', {
        'form': form,
        'titulo': 'Registrar Nuevo Producto',
        'accion': 'Guardar Producto',
        'es_edicion': False
    })


def editar_producto(request, pk):
    """
    Fase 6: Editar producto en /productos/editar/<id>/
    """
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡El producto "{producto.nombre}" fue actualizado con éxito!')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'inventario/formulario_producto.html', {
        'form': form,
        'producto': producto,
        'titulo': f'Editar Producto: {producto.nombre}',
        'accion': 'Actualizar Cambios',
        'es_edicion': True
    })


def eliminar_producto(request, pk):
    """
    Fase 6: Eliminar producto en /productos/eliminar/<id>/
    """
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre_prod = producto.nombre
        producto.delete()
        messages.warning(request, f'El producto "{nombre_prod}" ha sido eliminado del catálogo.')
        return redirect('lista_productos')

    return render(request, 'inventario/confirmar_eliminar.html', {'producto': producto})


def lista_categorias(request):
    """
    Gestión de categorías
    """
    categorias = Categoria.objects.annotate(num_productos=Count('productos')).all()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat = form.save()
            messages.success(request, f'Categoría "{cat.nombre}" agregada correctamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'inventario/lista_categorias.html', {
        'categorias': categorias,
        'form': form
    })
