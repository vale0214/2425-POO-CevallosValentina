# Definir la clase Clima, que representará las temperaturas de la semana
class Clima:
    def __init__(self):
        self.temperaturas = []  # Atributo para almacenar las temperaturas

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):  # Se ingresan 7 días de la semana
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        # Sumar todas las temperaturas y dividir entre la cantidad de días (7)
        return sum(self.temperaturas) / len(self.temperaturas)


# Clase principal que maneja la ejecución del sistema
class SistemaClima:
    def __init__(self):
        self.clima = Clima()  # Crear un objeto de la clase Clima para gestionar las temperaturas

    # Método para coordinar el flujo del programa
    def ejecutar(self):
        print("Bienvenido a la calculadora del promedio semanal de temperaturas.")

        # Ingresar las temperaturas usando el método de la clase Clima
        self.clima.ingresar_temperaturas()

        # Calcular el promedio usando el método de la clase Clima
        promedio = self.clima.calcular_promedio()

        # Mostrar el resultado del promedio
        print(f"El promedio de temperaturas de la semana es: {promedio:.2f}°C")


# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaClima()  # Crear una instancia del sistema
    sistema.ejecutar()  # Ejecutar el flujo del programa
