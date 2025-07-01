import sys, time, random, matplotlib.pyplot as plt
from testsGeneradores import *

# Verificar argumentos de línea de comandos
if len(sys.argv) != 5 or sys.argv[1] != "-s" or sys.argv[3] != "-n":
    print("Uso: Python randomPython.py -s <Semilla> -n <Cantidad>")
    print("Nota: Para usar hora actual como semilla, use \" \" como valor")
    sys.exit(1)

# Procesar argumentos
semilla = int(time.time()) if sys.argv[2] == " " else int(sys.argv[2])
cantidad = int(sys.argv[4])

def generar_random_python(semilla, n):
    """Genera números pseudoaleatorios usando el generador nativo de Python"""
    # Inicializar el generador con la semilla
    random.seed(semilla)
    
    # Generar n números entre 0 y 2^32-1 para mantener consistencia con otros generadores
    numeros = [random.randint(0, 2**32-1) for _ in range(n)]
    return numeros

# Generar los números
numeros = generar_random_python(semilla, cantidad)

# Mostrar resultados
print("\n>> Números generados:")
print(numeros)

# Ejecutar pruebas estadísticas
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
plt.figure(figsize=(10, 6))
plt.scatter(indices, numeros, s=10, c="purple")
plt.grid(True, alpha=0.3)
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Distribución de valores - Generador nativo de Python')
plt.show()