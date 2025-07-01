import sys, time, matplotlib.pyplot as plt
from testsGeneradores import *

if sys.argv[1] != "-s" or sys.argv[3] != "-n":
    print("Uso: Python randomMidSquare.py -s <Valor_Inicial> -n <Total>")
    print("Nota: Para usar hora actual como semilla, use \" \" como valor")
    sys.exit(1)

semilla = int(time.time()) if sys.argv[2] == " " else int(sys.argv[2])
cantidad = int(sys.argv[4])

def gen_mid_squares(semilla, n):
    """Implementa el método de cuadrados medios de von Neumann"""
    cuadrados = []
    semillas = []
    x0 = semilla
    valor_inicial = semilla
    
    for i in range(n):
        # Calcular cuadrado y agregarlo a la lista de resultados
        cuadrados.append(x0**2)
        
        # Preparar la siguiente semilla
        num_str = str(int(x0)**2).zfill(8)  # Completar con ceros a la izquierda
        
        if len(num_str) > 4:
            pos_inicio = (len(num_str) - 4) // 2
            
        # Extraer dígitos centrales para la nueva semilla
        x0 = int(num_str[pos_inicio:pos_inicio + 4])
        semillas.append(x0)
        
        # Verificar ciclo (cuando se repite un valor)
        if i > 0 and x0 == valor_inicial:
            print(f"Advertencia: Se encontró un ciclo después de {i+1} números")
            break
        
    return cuadrados, semillas

# Generar números
numeros, semillas = gen_mid_squares(semilla, cantidad)

print("\n>> Valores cuadrados:")
print(numeros)

print("\n>> Semillas generadas:")
print(semillas)

# Pruebas estadísticas
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
plt.figure(figsize=(8, 5))
plt.scatter(indices, numeros, s=10, c="darkgreen")
plt.grid(True, alpha=0.3)
plt.xlabel('Posición')
plt.ylabel('Valor')
plt.title('Distribución de valores - Método cuadrados medios')
plt.show()