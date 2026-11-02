# Evidencia 3: Laboratorio Catálogo de Productos con Django

**Unidad de Aprendizaje:** Fundamentos de Desarrollo Web  
**Estudiante:** César Enrique Reyes Zamora  
**Matrícula:** 2089628 | **Grupo:** 52  
**Docente:** Hiram Isaí Pérez Sauceda  
**Facultad:** Facultad de Contaduría Pública y Administración (FACPYA) - UANL  

---

## 📌 Descripción del Proyecto
Sistema web empresarial desarrollado con el framework **Django** bajo la arquitectura **MVT (Model - View - Template)** para la administración de un catálogo de productos con inventario y categorización comercial.

### Funcionalidades Implementadas:
- ✅ **Operaciones CRUD Completas:** Registrar, consultar, editar y eliminar productos (`/productos/`, `/productos/nuevo/`, `/productos/editar/<id>/`, `/productos/eliminar/<id>/`).
- ✅ **Módulo de Categorías:** Relación uno a muchos entre categorías y productos mediante `models.ForeignKey`.
- ✅ **Formularios con ModelForm:** Generación automática de inputs con validaciones personalizadas.
- ✅ **Búsqueda Avanzada:** Filtrado insensible a mayúsculas/minúsculas usando el lookup `nombre__icontains`.
- ✅ **Ordenamiento Dinámico:** Reordenamiento mediante `order_by('nombre')` y orden descendente `order_by('-precio')`.
- ✅ **Estadísticas de Negocio (ORM Aggregations):** Cálculo en tiempo real de cantidad de productos con `Count()`, existencias con `Sum()`, precio promedio con `Avg()` y valor total del inventario.
- ✅ **Panel Administrativo:** Configuración completa en `/admin/` para gestión de modelos.

---

## 🚀 Instrucciones de Instalación y Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/zamhs/catalogo-productos-django.git
   cd catalogo-productos-django
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. Instalar las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar las migraciones a la base de datos SQLite:
   ```bash
   python manage.py migrate
   ```

5. (Opcional) Poblar los datos de prueba (5 categorías y 17 productos):
   ```bash
   python poblar_datos.py
   ```

6. Iniciar el servidor de desarrollo de Django:
   ```bash
   python manage.py runserver
   ```

7. Abrir el navegador en:
   - **Catálogo Web:** [http://127.0.0.1:8000/productos/](http://127.0.0.1:8000/productos/)
   - **Panel Administrativo:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
     *(Usuario: `admin` | Contraseña: `admin12345`)*
