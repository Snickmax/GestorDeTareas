# Gestor de Tareas

Este es un proyecto en Python para gestionar tareas. Permite agregar, listar, marcar como completadas, eliminar tareas y guardarlas o cargarlas desde un archivo JSON. También utiliza una base de datos PostgreSQL para almacenar las tareas de forma persistente.

---

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interactuar con la base de datos PostgreSQL.
- **PostgreSQL**: Base de datos relacional para el almacenamiento persistente de tareas.
- **dotenv**: Para cargar las configuraciones desde un archivo `.env`.
- **psycopg2**: Controlador de PostgreSQL para Python.

---

## Estructura del Proyecto

```
.
├── main.py                     # Archivo principal para ejecutar la aplicación
├── app/                        # Módulo de la aplicación
│   ├── __init__.py             # Archivo de inicialización del módulo
│   ├── models.py               # Definición de la tabla y modelo de datos
│   └── controllers.py          # Controladores para gestionar la lógica de las tareas
├── config/                     # Configuraciones del proyecto
│   ├── __init__.py             # Archivo de inicialización del módulo
│   └── database.py             # Configuración de la base de datos
├── .env                        # Archivo de variables de entorno
└── requirements.txt            # Dependencias del proyecto
```

---

## Configuración del Proyecto

### 1. Pre-requisitos

- Python 3.8 o superior.
- PostgreSQL instalado y configurado.
- Un entorno virtual de Python (opcional, pero recomendado).

### 2. Configurar la Base de Datos

1. Crear una base de datos PostgreSQL llamada `desafio` (o el nombre que desees).
2. Configura las credenciales en un archivo `.env` en la raíz del proyecto:

```env
DB_NAME=desafio
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
```

### 3. Instalación

1. Clona el repositorio o descarga el código.
2. Crea un entorno virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate   # Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configura la base de datos:
   ```bash
   python migrate.py
   ```

### 4. Ejecutar el Proyecto

Ejecuta el archivo `main.py` para iniciar el programa:
```bash
python main.py
```

---

## Uso del Proyecto

1. **Agregar Tareas**: Ingresa un título y una descripción.
2. **Listar Tareas**: Visualiza todas las tareas con su estado (pendiente o completada).
3. **Marcar Tareas como Completadas**: Cambia el estado de una tarea.
4. **Eliminar Tareas**: Borra una tarea de la base de datos.
5. **Guardar Tareas en Archivo**: Exporta todas las tareas a un archivo JSON.
6. **Cargar Tareas desde Archivo**: Importa tareas desde un archivo JSON.

---

## Dependencias

Las dependencias se encuentran en el archivo `requirements.txt`. Para instalarlas, usa:
```bash
pip install -r requirements.txt
```

---

## Posibles Errores y Soluciones

1. **Error de conexión con la base de datos**:
   - Verifica que PostgreSQL esté ejecutándose y las credenciales en el archivo `.env` sean correctas.

2. **Archivo JSON no encontrado**:
   - Asegúrate de que el archivo existe en la ruta especificada.

3. **Paquetes no instalados**:
   - Verifica que instalaste las dependencias correctamente.


