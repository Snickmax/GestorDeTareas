from app.models import Tarea
from config.database import Session
import json

session = Session()

def agregar_tarea(titulo, descripcion):
    tarea = Tarea(titulo=titulo, descripcion=descripcion)
    session.add(tarea)
    session.commit()
    return f"Tarea '{titulo}' agregada correctamente."

def listar_tareas():
    tareas = session.query(Tarea).all()
    return [
        {
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion,
            "completada": "Completada" if tarea.completada else "Pendiente"
        }
        for tarea in tareas
    ]

def marcar_tarea_completada(tarea_id):
    tarea = session.query(Tarea).get(tarea_id)
    if not tarea:
        return "Tarea no encontrada."
    tarea.completada = True
    session.commit()
    return f"Tarea '{tarea.titulo}' marcada como completada."

def eliminar_tarea(tarea_id):
    tarea = session.query(Tarea).get(tarea_id)
    if not tarea:
        return "Tarea no encontrada."
    session.delete(tarea)
    session.commit()
    return f"Tarea '{tarea.titulo}' eliminada."

def guardar_tareas_en_archivo(nombre_archivo):
    tareas = listar_tareas()
    with open(nombre_archivo, 'w') as archivo:
        json.dump(tareas, archivo)
    return f"Tareas guardadas en {nombre_archivo}."

def cargar_tareas_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        for dato in datos:
            tarea = Tarea(
                id=dato["id"],
                titulo=dato["titulo"],
                descripcion=dato["descripcion"],
                completada=dato["completada"] == "Completada"
            )
            session.merge(tarea)
        session.commit()
        return f"Tareas cargadas desde {nombre_archivo}."
    except FileNotFoundError:
        return "Archivo no encontrado."