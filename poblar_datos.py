import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo_productos.settings')
django.setup()

from django.contrib.auth.models import User
from inventario.models import Categoria, Producto

# 1. Crear Superusuario para el panel de administración
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@uanl.edu.mx', 'admin12345')
    print("✓ Superusuario 'admin' creado exitosamente.")
else:
    print("• El superusuario 'admin' ya existe.")

# 2. Crear las 5 Categorías solicitadas en la Fase 4 Actividad 1
categorias_data = [
    {
        'nombre': 'Cómputo',
        'descripcion': 'Equipos de cómputo, laptops, servidores y componentes de procesamiento.'
    },
    {
        'nombre': 'Electrónica',
        'descripcion': 'Dispositivos electrónicos, pantallas, monitores, audio y video.'
    },
    {
        'nombre': 'Hogar',
        'descripcion': 'Artículos para el hogar, electrodomésticos, iluminación y climatización.'
    },
    {
        'nombre': 'Deportes',
        'descripcion': 'Artículos deportivos, accesorios de entrenamiento y acondicionamiento físico.'
    },
    {
        'nombre': 'Papelería',
        'descripcion': 'Materiales de oficina, consumibles de impresión, papel y papelería comercial.'
    },
]

cats_dict = {}
for cat_info in categorias_data:
    cat, created = Categoria.objects.get_or_create(
        nombre=cat_info['nombre'],
        defaults={'descripcion': cat_info['descripcion']}
    )
    cats_dict[cat.nombre] = cat
    estado = "creada" if created else "existente"
    print(f"• Categoría '{cat.nombre}' ({estado}).")

# 3. Registrar al menos 15 productos (Fase 4 Actividad 2)
productos_data = [
    # Cómputo
    {
        'nombre': 'Laptop HP 15-dy2061la',
        'descripcion': 'Laptop con procesador Intel Core i5, 8GB RAM y 512GB SSD NVMe.',
        'precio': 15000.00,
        'existencias': 12,
        'categoria': cats_dict['Cómputo']
    },
    {
        'nombre': 'Teclado Logitech G213 Prodigy',
        'descripcion': 'Teclado para juegos RGB con teclas mech-dome resistentes a salpicaduras.',
        'precio': 450.00,
        'existencias': 25,
        'categoria': cats_dict['Cómputo']
    },
    {
        'nombre': 'Mouse Inalámbrico Logitech M185',
        'descripcion': 'Mouse óptico inalámbrico 2.4 GHz compacto con receptor nano USB.',
        'precio': 299.00,
        'existencias': 30,
        'categoria': cats_dict['Cómputo']
    },
    {
        'nombre': 'Disco Sólido Kingston NV2 1TB',
        'descripcion': 'Unidad SSD M.2 PCIe 4.0 NVMe con velocidad de lectura de 3500MB/s.',
        'precio': 1350.00,
        'existencias': 18,
        'categoria': cats_dict['Cómputo']
    },
    # Electrónica
    {
        'nombre': 'Monitor Samsung 27 Curvo',
        'descripcion': 'Monitor curvo Full HD de 27 pulgadas, panel VA a 75Hz y tecnología FreeSync.',
        'precio': 3500.00,
        'existencias': 10,
        'categoria': cats_dict['Electrónica']
    },
    {
        'nombre': 'Impresora Epson EcoTank L3250',
        'descripcion': 'Impresora multifuncional de tanque de tinta continua con conectividad Wi-Fi.',
        'precio': 4200.00,
        'existencias': 8,
        'categoria': cats_dict['Electrónica']
    },
    {
        'nombre': 'Audífonos Bluetooth Sony WH-CH520',
        'descripcion': 'Audífonos inalámbricos de diadema con hasta 50 horas de batería.',
        'precio': 899.00,
        'existencias': 15,
        'categoria': cats_dict['Electrónica']
    },
    {
        'nombre': 'Bocina Inteligente Amazon Echo Dot 5ta Gen',
        'descripcion': 'Altavoz inteligente con asistente de voz Alexa y control de hogar.',
        'precio': 999.00,
        'existencias': 14,
        'categoria': cats_dict['Electrónica']
    },
    # Hogar
    {
        'nombre': 'Cafetera Programable Oster 12 Tazas',
        'descripcion': 'Cafetera eléctrica con filtro permanente, selector de intensidad y jarra de vidrio.',
        'precio': 850.00,
        'existencias': 16,
        'categoria': cats_dict['Hogar']
    },
    {
        'nombre': 'Freidora de Aire Ninja 4 Litros',
        'descripcion': 'Freidora digital con 4 funciones: freír con aire, asar, recalentar y deshidratar.',
        'precio': 2100.00,
        'existencias': 9,
        'categoria': cats_dict['Hogar']
    },
    {
        'nombre': 'Aspiradora Robot Xiaomi Vacuum E10',
        'descripcion': 'Robot aspirador y trapeador con potencia de 4000Pa y navegación giroscópica.',
        'precio': 3800.00,
        'existencias': 6,
        'categoria': cats_dict['Hogar']
    },
    # Deportes
    {
        'nombre': 'Mancuernas Ajustables 20kg Kit',
        'descripcion': 'Juego de mancuernas con discos de hierro fundido y barra extensora conector.',
        'precio': 1200.00,
        'existencias': 11,
        'categoria': cats_dict['Deportes']
    },
    {
        'nombre': 'Tapete para Yoga Antideslizante 6mm',
        'descripcion': 'Colchoneta de ejercicio de material TPE ecológico de alta densidad con correa.',
        'precio': 420.00,
        'existencias': 22,
        'categoria': cats_dict['Deportes']
    },
    {
        'nombre': 'Cuerda para Saltar de Alta Velocidad',
        'descripcion': 'Cuerda de acero recubierta de PVC con baleros metálicos giratorios de 360 grados.',
        'precio': 190.00,
        'existencias': 35,
        'categoria': cats_dict['Deportes']
    },
    # Papelería
    {
        'nombre': 'Caja de Papel Bond Xerox Carta 5000 Hojas',
        'descripcion': 'Caja con 10 paquetes de 500 hojas de papel bond blanco de 75 gramos tamaño carta.',
        'precio': 980.00,
        'existencias': 20,
        'categoria': cats_dict['Papelería']
    },
    {
        'nombre': 'Paquete Bolígrafos Bic Cristal 12 Piezas',
        'descripcion': 'Bolígrafos de punto mediano 1.0mm con tinta de secado rápido color azul.',
        'precio': 95.00,
        'existencias': 50,
        'categoria': cats_dict['Papelería']
    },
    {
        'nombre': 'Engrapadora de Uso Rudo Bostitch',
        'descripcion': 'Engrapadora metálica de palanca con capacidad para grapar hasta 60 hojas juntas.',
        'precio': 380.00,
        'existencias': 14,
        'categoria': cats_dict['Papelería']
    }
]

for p_data in productos_data:
    p, created = Producto.objects.get_or_create(
        nombre=p_data['nombre'],
        defaults={
            'descripcion': p_data['descripcion'],
            'precio': p_data['precio'],
            'existencias': p_data['existencias'],
            'categoria': p_data['categoria']
        }
    )
    estado = "creado" if created else "existente"
    print(f"✓ Producto '{p.nombre}' (${p.precio}) - {estado}.")

print(f"\n🎉 Base de datos poblada exitosamente:")
print(f"   Total Categorías: {Categoria.objects.count()}")
print(f"   Total Productos: {Producto.objects.count()}")
