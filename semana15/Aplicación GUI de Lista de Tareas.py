import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Escribe una tarea antes de añadirla.")

def marcar_completada():
    try:
        seleccion = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(seleccion)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(seleccion)
            lista_tareas.insert(seleccion, "✔ " + tarea)
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para marcarla como completada.")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para eliminar.")

# Configurar ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada
tk.Label(root, text="Nueva Tarea:").pack(pady=5)
entrada_tarea = tk.Entry(root, width=50)
entrada_tarea.pack(pady=5)
entrada_tarea.bind("<Return>", agregar_tarea)  # Añadir tarea con Enter

# Listbox para tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(pady=10)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack()

tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Marcar Completada", command=marcar_completada).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea).grid(row=0, column=2, padx=5)

# Ejecutar aplicación
root.mainloop()
