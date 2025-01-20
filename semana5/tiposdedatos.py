# Programa para calcular el área de un círculo y un cuadrado
# Este programa solicita al usuario los datos necesarios para calcular las áreas de un círculo y un cuadrado.

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    return math.pi * radio ** 2


def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado su lado.
    :param lado: Longitud del lado del cuadrado (float)
    :return: Área del cuadrado (float)
    """
    return lado ** 2


def main():
    """
    Función principal que interactúa con el usuario para obtener las dimensiones y calcular las áreas.
    """
    print("Bienvenido al programa de cálculo de áreas!")

    # Solicitar el radio del círculo
    radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
    area_circulo = calcular_area_circulo(radio_circulo)

    # Solicitar el lado del cuadrado
    lado_cuadrado = float(input("Por favor, ingrese la longitud del lado del cuadrado: "))
    area_cuadrado = calcular_area_cuadrado(lado_cuadrado)

    # Mostrar los resultados
    print(f"\nResultados:")
    print(f"El área del círculo con radio {radio_circulo} es: {area_circulo:.2f}")
    print(f"El área del cuadrado con lado {lado_cuadrado} es: {area_cuadrado:.2f}")

    # Verificar si las áreas son iguales (ejemplo de uso de boolean)
    areas_iguales = area_circulo == area_cuadrado
    if areas_iguales:
        print("Las áreas del círculo y el cuadrado son iguales.")
    else:
        print("Las áreas del círculo y el cuadrado son diferentes.")


if __name__ == "__main__":
    main()
