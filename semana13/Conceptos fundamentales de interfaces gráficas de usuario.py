import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Datos Simple")
root.geometry("400x300")  # Tamaño de la ventana

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada.delete(0, tk.END)  # Limpiar campo de texto después de agregar
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese un dato antes de agregar.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Etiqueta
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto
entrada = tk.Entry(root, width=30)
entrada.pack()

# Botón Agregar
btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(root, width=40, height=10)
lista_datos.pack(pady=10)

# Botón Limpiar
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack()

# Ejecutar la aplicación
root.mainloop()
