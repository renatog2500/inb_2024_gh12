import random

def operacion_rara(numero):
    resultado = numero ** 3 + 2 * numero - 1
    return resultado

def generar_numeros_aleatorios(cantidad):
    numeros = []
    for _ in range(cantidad):
        numeros.append(random.randint(1, 100))
    return numeros

if __name__ == "__main__":
    cantidad_numeros = 10
    numeros_aleatorios = generar_numeros_aleatorios(cantidad_numeros)

    print("Números aleatorios generados:")
    print(numeros_aleatorios)
    print("\nOperaciones raras realizadas:")
    for numero in numeros_aleatorios:
        resultado = operacion_rara(numero)
        print(f"Operación con {numero}: {resultado}")
