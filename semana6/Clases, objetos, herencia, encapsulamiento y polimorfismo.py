#Clase herencia objetos encapsulamiento y polimorfismo
# Clase base: Mascota
class Mascota:
    def __init__(self, nombre, edad):
        # Atributos protegidos para demostrar encapsulación
        self._nombre = nombre
        self._edad = edad

    def mostrar_informacion(self):
        """Método para mostrar información básica de la mascota."""
        return f"Nombre: {self._nombre}, Edad: {self._edad} años"

    def hacer_sonido(self):
        """Método genérico para demostrar polimorfismo."""
        return "La mascota hace un sonido genérico."

# Clase derivada: Perro
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    def hacer_sonido(self):
        return "guau guau!"

    def mostrar_informacion(self):
        """Extender el método para incluir información específica del perro."""
        info_base = super().mostrar_informacion()
        return f"{info_base}, Raza: {self.raza}"

# Clase derivada: Gato
class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color


    def hacer_sonido(self):
        return "miau miau!"

    def mostrar_informacion(self):
        """Extender el método para incluir información específica del gato."""
        info_base = super().mostrar_informacion()
        return f"{info_base}, Color: {self.color}"

# Programa principal
def main():
    # Crear instancias de las clases
    mi_perro = Perro("coffy", 3, "Labrador")
    mi_gato = Gato("gorda", 2, "Blanco")

    # Mostrar información y sonidos de las mascotas
    print(mi_perro.mostrar_informacion())
    print(mi_perro.hacer_sonido())

    print(mi_gato.mostrar_informacion())
    print(mi_gato.hacer_sonido())

# Ejecutar el programa
if __name__ == "__main__":
    main()
