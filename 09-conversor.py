#!/usr/bin/env python3

"""Conversor completo de temperaturas entre múltiples escalas."""

# Diccionario con las unidades disponibles y su etiqueta de impresión.
UNIDADES = {
    "C": "Celsius",
    "F": "Fahrenheit",
    "K": "Kelvin",
    "R": "Rankine",
    "Re": "Réaumur",
}


def mostrar_menu_unidades():
    """Muestra las opciones de unidades disponibles."""
    print("\n=== CONVERSOR DE TEMPERATURAS Neils33Arquitec ===")
    for codigo, nombre in UNIDADES.items():
        print(f"{codigo}: {nombre}")
    print("S: Salir")


def pedir_unidad(prompt):
    """Pide una unidad al usuario y la valida."""
    while True:
        unidad = input(prompt).strip().capitalize().replace("º", "")
        if unidad in UNIDADES:
            return unidad
        if unidad.lower() == "s":
            return "S"
        print("Unidad no válida. Usa C, F, K, R o Re.")


def pedir_temperatura(unidad_origen):
    """Pide la temperatura en la unidad de origen y la convierte a float."""
    while True:
        entrada = input(
            f"Ingresa la temperatura en {UNIDADES[unidad_origen]} ({unidad_origen}): ")
        try:
            return float(entrada.replace(",", "."))
        except ValueError:
            print("Entrada no válida. Ingresa un número, por ejemplo 25 o -3.5.")


def a_kelvin(valor, unidad):
    """Convierte un valor de la unidad dada a Kelvin."""
    if unidad == "C":
        return valor + 273.15
    if unidad == "F":
        return (valor + 459.67) * 5 / 9
    if unidad == "K":
        return valor
    if unidad == "R":
        return valor * 5 / 9
    if unidad == "Re":
        return valor * 5 / 4 + 273.15
    raise ValueError(f"Unidad desconocida: {unidad}")


def desde_kelvin(valor_kelvin, unidad):
    """Convierte un valor en Kelvin a la unidad indicada."""
    if unidad == "C":
        return valor_kelvin - 273.15
    if unidad == "F":
        return valor_kelvin * 9 / 5 - 459.67
    if unidad == "K":
        return valor_kelvin
    if unidad == "R":
        return valor_kelvin * 9 / 5
    if unidad == "Re":
        return (valor_kelvin - 273.15) * 4 / 5
    raise ValueError(f"Unidad desconocida: {unidad}")


def convertir(valor, origen, destino):
    """Convierte una temperatura de una unidad origen a una unidad destino."""
    kelvin = a_kelvin(valor, origen)
    return desde_kelvin(kelvin, destino)


def pedir_continuar():
    """Pregunta al usuario si desea realizar otra conversión."""
    while True:
        respuesta = input(
            "¿Deseas realizar otra operación? (S/N): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Por favor responde S para sí o N para no.")


def main():
    while True:
        mostrar_menu_unidades()

        unidad_origen = pedir_unidad("Selecciona la unidad de origen: ")
        if unidad_origen == "S":
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break

        unidad_destino = pedir_unidad("Selecciona la unidad de destino: ")
        if unidad_destino == "S":
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break

        if unidad_destino == unidad_origen:
            print(
                "La unidad de origen y destino es la misma. El resultado será el mismo valor.")

        temperatura = pedir_temperatura(unidad_origen)
        resultado = convertir(temperatura, unidad_origen, unidad_destino)

        print(
            f"{temperatura:.2f} {unidad_origen} ({UNIDADES[unidad_origen]}) "
            f"= {resultado:.2f} {unidad_destino} ({UNIDADES[unidad_destino]})"
        )

        if not pedir_continuar():
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
