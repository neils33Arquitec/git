#!/usr/bin/env python3

"""Conversor de temperaturas desde Celsius a otras magnitudes."""


def mostrar_menu():
    print("\n=== CONVERSOR DE TEMPERATURAS Neils33Arquitec===")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Celsius a Rankine")
    print("4. Celsius a Réaumur")
    print("5. Salir")


def convertir_celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def convertir_celsius_a_kelvin(celsius):
    return celsius + 273.15


def convertir_celsius_a_rankine(celsius):
    return (celsius + 273.15) * 9 / 5


def convertir_celsius_a_reaumur(celsius):
    return celsius * 4 / 5


def pedir_temperatura():
    while True:
        entrada = input("Ingresa la temperatura en Celsius: ")
        try:
            return float(entrada.replace(",", "."))
        except ValueError:
            print("Entrada no válida. Ingresa un número, por ejemplo 25 o -3.5.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            celsius = pedir_temperatura()
            resultado = convertir_celsius_a_fahrenheit(celsius)
            print(f"{celsius:.2f} °C = {resultado:.2f} °F")
        elif opcion == "2":
            celsius = pedir_temperatura()
            resultado = convertir_celsius_a_kelvin(celsius)
            print(f"{celsius:.2f} °C = {resultado:.2f} K")
        elif opcion == "3":
            celsius = pedir_temperatura()
            resultado = convertir_celsius_a_rankine(celsius)
            print(f"{celsius:.2f} °C = {resultado:.2f} °R")
        elif opcion == "4":
            celsius = pedir_temperatura()
            resultado = convertir_celsius_a_reaumur(celsius)
            print(f"{celsius:.2f} °C = {resultado:.2f} °Ré")
        elif opcion == "5":
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige un número entre 1 y 5.")


if __name__ == "__main__":
    main()
