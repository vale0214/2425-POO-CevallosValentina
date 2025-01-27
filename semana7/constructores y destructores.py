# Programa que demuestra el uso de constructores (__init__) y destructores (__del__) en Python

class Auto:
    """
    Clase para simular las acciones relacionadas con el auto de Valentina.
    """
    def __init__(self, marca, modelo, año):
        """
        Constructor: Se ejecuta al crear una instancia de la clase.
        Inicializa los atributos del auto: marca, modelo y año.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        print(f"Auto de Valentina creado: {self.marca} {self.modelo} ({self.año}).")

    def encender(self):
        """
        Método para simular el encendido del auto.
        """
        print(f"El auto {self.marca} {self.modelo} está encendido.")

    def conducir(self, destino):
        """
        Método para simular la conducción del auto hacia un destino.
        """
        print(f"Conduciendo el {self.marca} {self.modelo} hacia {destino}.")

    def __del__(self):
        """
        Destructor: Se ejecuta automáticamente cuando el objeto es eliminado.
        Simula apagar el auto y liberar recursos.
        """
        print(f"El auto {self.marca} {self.modelo} ha sido apagado y los recursos han sido liberados.")

# Demostración del uso de constructores y destructores
if __name__ == "__main__":
    # Crear una instancia de la clase Auto
    auto_valentina = Auto("Ford", "Explorer", 2013)

    # Encender el auto
    auto_valentina.encender()

    # Conducir el auto a un destino
    auto_valentina.conducir("la universidad")

    # El objeto auto_valentina será destruido automáticamente al final del programa
    # o si se elimina explícitamente usando del
    del auto_valentina  # Llamada explícita al destructor

    print("Fin del programa. El destructor debería haberse llamado.")
