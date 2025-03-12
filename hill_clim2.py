import numpy as np
import matplotlib.pyplot as plt
import random

# Definir la función objetivo
def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9  # Función cuadrática con máximo en x=3

# Algoritmo Hill Climbing con impresión de pasoss

def hill_climbing(paso=0.1, iteraciones=50):
    x_actual = random.uniform(-10, 10)  # Selección de un punto aleatorio
    mejor_valor = funcion_objetivo(x_actual)
    
    historial_x = [x_actual]  # Para almacenar los valores explorados
    historial_y = [mejor_valor]

    print("\nIteración |  x_actual  |  f(x_actual)  |  x_vecino  |  f(x_vecino)  |  Mejorado?")
    print("-" * 80)

    for i in range(iteraciones):
        vecino = x_actual + random.choice([-paso, paso])  # Moverse en una dirección aleatoria
        valor_vecino = funcion_objetivo(vecino)

        mejorado = valor_vecino > mejor_valor  # Verificar si es una mejora
        print(f"{i+1:9} | {x_actual:9.4f} | {mejor_valor:12.4f} | {vecino:9.4f} | {valor_vecino:12.4f} | {'Sí' if mejorado else 'No'}")

        if mejorado:  # Si el vecino es mejor, actualizar
            x_actual = vecino
            mejor_valor = valor_vecino
            historial_x.append(x_actual)
            historial_y.append(mejor_valor)

    return x_actual, mejor_valor, historial_x, historial_y

# Ejecutar el algoritmo
mejor_x, mejor_y, historial_x, historial_y = hill_climbing()

# Graficar la función
x = np.linspace(-10, 10, 400)
y = funcion_objetivo(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Función Objetivo", color="blue")

# Graficar puntos explorados
plt.scatter(historial_x, historial_y, color="red", marker="o", label="Exploración")

# Marcar el máximo encontrado
plt.scatter([mejor_x], [mejor_y], color="green", marker="*", s=200, label="Máximo Encontrado")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Búsqueda de Máximo con Hill Climbing")
plt.legend()
plt.grid()
plt.show()

print("\nHistorial de valores explorados:")
print("x:", historial_x)
print("f(x):", historial_y)
print(f"\nMáximo encontrado en x = {mejor_x:.4f}, f(x) = {mejor_y:.4f}")