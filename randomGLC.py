import time, sys, matplotlib.pyplot as plt
from testsGeneradores import *

if sys.argv[1]!="-s" or sys.argv[3]!="-a" or sys.argv[5]!="-c" or sys.argv[7]!="-m" or sys.argv[9]!="-n":
    print("Uso: Python randomGLC.py -s <Semilla> -a <Multiplicador> -c <Incremento> -m <Módulo> -n <Cantidad>")
    print("Para tiempo actual como semilla use \" \" como valor")
    sys.exit(1)

semilla = int(time.time()) if sys.argv[2] == " " else int(sys.argv[2])
multiplicador = int(sys.argv[4])
incremento = int(sys.argv[6])
modulo = int(eval(sys.argv[8]))
cantidad = int(sys.argv[10])

def generar_lcg(a, c, m, x0, n):
    """Genera números usando el método congruencial lineal (a*x + c) mod m"""
    nums = []
    valor_inicial = x0
    
    # Verificar que los parámetros cumplan las condiciones
    if not (m > 0 and a > 0 and a < m and c >= 0 and c < m and x0 >= 0 and x0 < m):
        print("Error: Los parámetros no cumplen las condiciones necesarias")
        return nums
    
    # Generar n números
    for i in range(n):
        # Aplicar la fórmula congruencial
        x0 = (a * x0 + c) % m
        nums.append(x0)
        
        # Verificar ciclo (si volvemos a la semilla original)
        if i > 0 and x0 == valor_inicial:
            print(f"Advertencia: Se encontró un ciclo después de {i+1} números")
            break
            
    return nums

# Ejecución principal
numeros = generar_lcg(multiplicador, incremento, modulo, semilla, cantidad)

print("\n>> Números generados:")
print(numeros)

print("\n>> Test de Frecuencia:")
testFrecuencia(numeros)

print("\n>> Test Chi Cuadrado:")
testChiCuadrado(numeros, cantidad)

print("\n>> Test Póker:")
testPoker(numeros, cantidad)

print("\n>> Test Rachas:")
testRachas(numeros, cantidad)

# Visualización
indices = list(range(cantidad))
plt.scatter(indices, numeros, s=10, c="navy")
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Distribución de valores generados')
plt.grid(alpha=0.3)
plt.show()