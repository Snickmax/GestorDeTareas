# Gestor de Tareas

- Victor Ignacio Ibarra Espinoza
Este es un proyecto en Python para gestionar tareas. Permite agregar, listar, marcar como completadas, eliminar tareas y guardarlas o cargarlas desde un archivo JSON. También utiliza una base de datos PostgreSQL para almacenar las tareas de forma persistente.

---

## Tecnologías Utilizadas

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto, utilizado para desarrollar la lógica del gestor de tareas.
- **Tkinter**: Biblioteca estándar de Python para la creación de interfaces gráficas de usuario (GUI).
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interactuar con la base de datos PostgreSQL, facilitando el trabajo con objetos en lugar de consultas SQL directas.
- **PostgreSQL**: Base de datos relacional utilizada para el almacenamiento persistente de tareas, proporcionando un almacenamiento estructurado y seguro.
- **dotenv**: Permite cargar configuraciones desde un archivo `.env`, facilitando la gestión de variables de entorno como las credenciales de la base de datos y otros parámetros sensibles.
- **psycopg2**: Controlador de PostgreSQL para Python, usado para la comunicación directa con la base de datos desde Python.

---

## Estructura del Proyecto

```
.
├── main.py                     # Archivo principal para ejecutar la aplicación
├── migrate.py                     # Archivo para migrar base de datos
├── app/                        # Módulo de la aplicación
│   ├── models.py               # Definición de la tabla y modelo de datos
│   ├── controllers.py          # Controladores para gestionar la lógica de las tareas
│   └── ui.py                   # Interfaz gráfica de usuario
├── config/                     # Configuraciones del proyecto
│   └── database.py             # Configuración de la base de datos
├── .env                        # Archivo de variables de entorno
└── requirements.txt            # Dependencias del proyecto

```

---

## Configuración del Proyecto

### 1. Pre-requisitos

- Python 3.12 ideal.
- PostgreSQL instalado y configurado.
- Un entorno virtual de Python (opcional, pero recomendado).

### 2. Configurar la Base de Datos si usas postgreSQL

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
   python virtualenv venv
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
