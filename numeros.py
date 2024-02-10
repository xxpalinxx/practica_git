import math

def superficie(radio):
    radio = float(input("Ingrese el valor: "))
    resultado = math.pi*(radio**2)
    return resultado

x = superficie(3.5)
print(f"La superficie del circulo es {x}")