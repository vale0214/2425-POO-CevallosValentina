import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía")

def mark_completed(event=None):
    try:
        selected_index = listbox.curselection()[0]
        task_text = listbox.get(selected_index)
        if not task_text.startswith("[✓] "):
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"[✓] {task_text}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def delete_task(event=None):
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def close_app(event=None):
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Entrada de texto
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)  # Atajo de teclado para agregar tarea

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Botones
btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack()

btn_complete = tk.Button(root, text="Marcar Completada", command=mark_completed)
btn_complete.pack()

btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack()

# Atajos de teclado
root.bind("<c>", mark_completed)  # Tecla "C" para marcar como completada
root.bind("<d>", delete_task)  # Tecla "D" para eliminar tarea
root.bind("<Delete>", delete_task)  # Tecla "Delete" para eliminar tarea
root.bind("<Escape>", close_app)  # Tecla "Escape" para cerrar la aplicación

# Iniciar la aplicación
root.mainloop()
