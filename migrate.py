from config.database import Base, engine
from app.models import Tarea

# Crear las tablas
Base.metadata.create_all(bind=engine)
print("Tablas creadas correctamente.")
