import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Este es el DatePicker que usaremos

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# --------- FRAMES ---------
# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10, fill=tk.BOTH, expand=True)

# Frame para la entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# --------- TREEVIEW ---------
# Crear TreeView para mostrar eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill=tk.BOTH, expand=True)

# --------- ENTRADAS ---------
# Etiqueta y campo de Fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
fecha_entry = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy')
fecha_entry.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de Hora
tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=0, column=3, padx=5, pady=5)

# Etiqueta y campo de Descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
descripcion_entry = tk.Entry(frame_entrada, width=40)
descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)


# --------- FUNCIONES ---------
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        # Insertar el evento en el TreeView
        tree.insert("", "end", values=(fecha, hora, descripcion))
        # Limpiar los campos de entrada
        hora_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")


def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar el evento seleccionado?"):
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Ninguna selección", "Por favor selecciona un evento para eliminar.")


def salir():
    root.quit()


# --------- BOTONES ---------
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# --------- MAIN LOOP ---------
root.mainloop()
