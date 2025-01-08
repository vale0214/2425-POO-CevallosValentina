# calcular las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []  # codigo para almacenar las temperaturas
    for i in range(7):  # ingresar 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


# codigo para calcular el promedio semanal
def calcular_promedio(temperaturas):
    # Sumar todas las temperaturas y dividir entre la cantidad de días (7)
    return sum(temperaturas) / len(temperaturas)


# Función principal que coordina el flujo del programa
def main():
    print("Bienvenido a la calculadora del promedio semanal de temperaturas.")

    # Ingresar las temperaturas usando la función correspondiente
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio usando la función correspondiente
    promedio = calcular_promedio(temperaturas)

    # Mostrar el resultado del promedio
    print(f"El promedio de temperaturas de la semana es: {promedio:.2f}°C")


# Ejecutar la función principal solo si el script es ejecutado directamente
if __name__ == "__main__":
    main()
