import os
import json

class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga el inventario desde el archivo si existe."""
        if os.path.exists(self.ARCHIVO_INVENTARIO):
            try:
                with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                    self.productos = json.load(archivo)
            except (FileNotFoundError, json.JSONDecodeError):
                print(" Error al leer el archivo. Se inicializa un inventario vacío.")
                self.productos = {}
            except PermissionError:
                print(" No tienes permisos para leer el archivo.")
        else:
            self.guardar_en_archivo()

    def guardar_en_archivo(self):
        """Guarda el inventario actual en el archivo."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                json.dump(self.productos, archivo, indent=4)
        except PermissionError:
            print(" No tienes permisos para escribir en el archivo.")

    def agregar_producto(self, nombre, cantidad):
        """Añade un producto al inventario o actualiza su cantidad."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_en_archivo()
        print(f" Producto '{nombre}' agregado o actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_en_archivo()
            print(f" Producto '{nombre}' eliminado correctamente.")
        else:
            print(f" El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra el inventario actual."""
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print(" Inventario Actual:")
            for nombre, cantidad in self.productos.items():
                print(f"- {nombre}: {cantidad}")

# Función de interfaz en consola
def menu():
    inventario = Inventario()
    while True:
        print("\n Menú de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                inventario.agregar_producto(nombre, cantidad)
            except ValueError:
                print(" Ingrese un número válido para la cantidad.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "3":
            inventario.mostrar_inventario()

        elif opcion == "4":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
