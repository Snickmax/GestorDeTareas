import tkinter as tk
from tkinter import messagebox
from app.controllers import (
    agregar_tarea, listar_tareas, marcar_tarea_completada, eliminar_tarea,
    guardar_tareas_en_archivo, cargar_tareas_desde_archivo
)

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        
        # Menú principal
        tk.Label(self.root, text="Gestor de Tareas", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Agregar Tarea", command=self.open_add_task_window, width=30).pack(pady=5)
        tk.Button(self.root, text="Listar Tareas", command=self.open_list_tasks_window, width=30).pack(pady=5)
        tk.Button(self.root, text="Marcar Tarea como Completada", command=self.open_mark_task_window, width=30).pack(pady=5)
        tk.Button(self.root, text="Eliminar Tarea", command=self.open_delete_task_window, width=30).pack(pady=5)
        tk.Button(self.root, text="Guardar Backup", command=self.save_backup, width=30).pack(pady=5)
        tk.Button(self.root, text="Cargar Backup", command=self.load_backup, width=30).pack(pady=5)

    def open_add_task_window(self):
        window = tk.Toplevel(self.root)
        window.title("Agregar Tarea")
        
        tk.Label(window, text="Título:").grid(row=0, column=0, padx=10, pady=5)
        title_entry = tk.Entry(window, width=40)
        title_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(window, text="Descripción:").grid(row=1, column=0, padx=10, pady=5)
        description_entry = tk.Entry(window, width=40)
        description_entry.grid(row=1, column=1, padx=10, pady=5)
        
        def add_task():
            title = title_entry.get()
            description = description_entry.get()
            if title.strip():
                message = agregar_tarea(title, description)
                messagebox.showinfo("Información", message)
                window.destroy()
            else:
                messagebox.showwarning("Advertencia", "El título no puede estar vacío.")
        
        tk.Button(window, text="Agregar", command=add_task).grid(row=2, column=0, columnspan=2, pady=10)

    def open_list_tasks_window(self):
        window = tk.Toplevel(self.root)
        window.title("Listar Tareas")
        
        text_area = tk.Text(window, width=60, height=20, state=tk.DISABLED)
        text_area.pack(padx=10, pady=10)

        tasks = listar_tareas()
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        for task in tasks:
            text_area.insert(tk.END, f"ID: {task['id']}, Título: {task['titulo']}, Estado: {task['completada']}\n    Descripción: {task['descripcion']}\n\n")
        text_area.config(state=tk.DISABLED)

    def open_mark_task_window(self):
        self.open_task_selection_window("Marcar como Completada", marcar_tarea_completada)

    def open_delete_task_window(self):
        self.open_task_selection_window("Eliminar Tarea", eliminar_tarea)

    def open_task_selection_window(self, title, action):
        window = tk.Toplevel(self.root)
        window.title(title)
        
        tk.Label(window, text="Seleccione una tarea de la lista:").pack(pady=5)
        task_listbox = tk.Listbox(window, width=60, height=15)
        task_listbox.pack(padx=10, pady=5)

        tasks = listar_tareas()
        task_mapping = {}
        for task in tasks:
            task_mapping[f"ID: {task['id']}, {task['titulo']} ({task['completada']})"] = task['id']
            task_listbox.insert(tk.END, f"ID: {task['id']}, {task['titulo']} ({task['completada']})")

        def execute_action():
            selected = task_listbox.curselection()
            if selected:
                task_text = task_listbox.get(selected[0])
                task_id = task_mapping[task_text]
                message = action(task_id)
                messagebox.showinfo("Información", message)
                window.destroy()
            else:
                messagebox.showwarning("Advertencia", "Seleccione una tarea.")

        tk.Button(window, text="Confirmar", command=execute_action).pack(pady=10)

    def save_backup(self):
        file_name = "backup_tareas.json"
        message = guardar_tareas_en_archivo(file_name)
        messagebox.showinfo("Información", message)

    def load_backup(self):
        file_name = "backup_tareas.json"
        message = cargar_tareas_desde_archivo(file_name)
        messagebox.showinfo("Información", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()