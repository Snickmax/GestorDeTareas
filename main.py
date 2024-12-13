from app.controllers import (
    agregar_tarea, listar_tareas, marcar_tarea_completada, eliminar_tarea,
    guardar_tareas_en_archivo, cargar_tareas_desde_archivo
)

def menu():
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Marcar Tarea como Completada")
        print("4. Eliminar Tarea")
        print("5. Guardar Tareas en Archivo")
        print("6. Cargar Tareas desde Archivo")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                titulo = input("Título de la tarea: ")
                descripcion = input("Descripción de la tarea: ")
                print(agregar_tarea(titulo, descripcion))
            case "2":
                tareas = listar_tareas()
                for tarea in tareas:
                    print(f"ID: {tarea['id']}, Título: {tarea['titulo']}, Estado: {tarea['completada']}")
                    print(f"    Descripcion: {tarea['descripcion']}\n")
            case "3":
                try:
                    tarea_id = int(input("ID de la tarea a completar: "))
                    print(marcar_tarea_completada(tarea_id))
                except ValueError:
                    print("Por favor ingrese un número válido para el ID de la tarea.")
            case "4":
                try:
                    tarea_id = int(input("ID de la tarea a eliminar: "))
                    print(eliminar_tarea(tarea_id))
                except ValueError:
                    print("Por favor ingrese un número válido para el ID de la tarea.")
            case "5":
                nombre_archivo = input("Nombre del archivo: ")
                print(guardar_tareas_en_archivo(nombre_archivo))
            case "6":
                nombre_archivo = input("Nombre del archivo: ")
                print(cargar_tareas_desde_archivo(nombre_archivo))
            case "7":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
