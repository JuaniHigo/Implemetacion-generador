"""Módulo con pruebas estadísticas para verificar aleatoriedad"""
import math
from collections import Counter
import numpy as np
from scipy.stats import chisquare

def testFrecuencia(nums):
    """Evalua si los dígitos siguen una distribución uniforme"""
    # Contar dígitos
    total = 0
    frec = [0] * 10
    
    for num in nums:
        for d in str(num):
            frec[int(d)] += 1
            total += 1
    
    # Normalizar frecuencias
    for i in range(10):
        frec[i] = frec[i] / total
    
    # Prueba estadística
    chi2, p = chisquare(frec, [0.1] * 10)

    print(f"Chi²: {chi2:.4f}, p-valor: {p:.4f}")
    
    if p < 0.05:
        print("❌ Los dígitos no siguen distribución uniforme")
    else:
        print("✅ Los dígitos siguen distribución uniforme")

def testChiCuadrado(nums, n):
    """Prueba la uniformidad en la distribución de valores"""
    # Dividir en 10 intervalos y contar
    obs_freq, _ = np.histogram(nums, bins=10)
    exp_freq = np.full(10, n / 10) # Esperado: distribución uniforme
    
    # Prueba estadística
    chi2, p = chisquare(obs_freq, exp_freq)
    
    print(f"Chi²: {chi2:.4f}, p-valor: {p:.4f}")
    
    if p > 0.05:
        print("✅ Los valores siguen distribución uniforme")
    else:
        print("❌ Los valores no siguen distribución uniforme")


def testPoker(nums, n):
    """Test de Póker para analizar patrones de dígitos"""
    # Normalizar los números a 5 dígitos
    nums_normalizados = []
    for num in nums:
        # Convertir a string, obtener los últimos 5 dígitos y rellenar con ceros si es necesario
        num_str = str(abs(num) % 100000).zfill(5)
        if len(num_str) > 5:
            num_str = num_str[-5:] # Tomar solo los últimos 5 dígitos
        nums_normalizados.append(num_str)
    
    # Usar la lista normalizada para el análisis
    nums = nums_normalizados
    
    # Clasificar números
    def clasificar(valores):
        clases = {
            "todos_dif": 0, "un_par": 0, "dos_pares": 0, 
            "trio": 0, "full": 0, "poker": 0, "quintilla": 0
        }
        
        for num in valores:
            conteo = Counter(str(num))
            patron = sorted(conteo.values(), reverse=True)
            
            if patron == [5]:             # Cinco iguales
                clases["quintilla"] += 1
            elif patron == [4, 1]:        # Cuatro iguales
                clases["poker"] += 1
            elif patron == [3, 2]:        # Full house
                clases["full"] += 1
            elif patron == [3, 1, 1]:     # Trío
                clases["trio"] += 1
            elif patron == [2, 2, 1]:     # Dos pares
                clases["dos_pares"] += 1
            elif patron == [2, 1, 1, 1]:  # Un par
                clases["un_par"] += 1
            else:                        # Todos diferentes
                clases["todos_dif"] += 1
        return clases
    
    # Probabilidades teóricas
    prob = {
        "todos_dif": 0.3024, "un_par": 0.504, "dos_pares": 0.108,
        "trio": 0.072, "full": 0.009, "poker": 0.0045, "quintilla": 0.0001
    }
    
    # Análisis
    obs = clasificar(nums)
    esp = {k: n * v for k, v in prob.items()}
    
    chi2, p = chisquare(list(obs.values()), f_exp=list(esp.values()))
    
    print(f"Chi²: {chi2:.4f}, p-valor: {p:.4f}")
    
    if p < 0.05:
        print("❌ Distribución de patrones no aleatoria")
    else:
        print("✅ Distribución de patrones aleatoria")



def testRachas(nums, n):
    """Analiza tendencias (rachas) para evaluar independencia"""
    # Contar rachas
    def contar_rachas(valores):
        rachas = 1  # Primera racha
        for i in range(1, len(valores)):
            if i >= 2 and ((valores[i] > valores[i-1] and valores[i-1] <= valores[i-2]) or 
                           (valores[i] < valores[i-1] and valores[i-1] >= valores[i-2])):
                rachas += 1
        return rachas
    
    # Calcular estadístico Z
    def calc_z(rachas, n):
        media = (2 * n - 1) / 3
        std = math.sqrt((16 * n - 29) / 90)
        return (rachas - media) / std
    
    # Análisis
    rachas = contar_rachas(nums)
    z = calc_z(rachas, n)
    
    print(f"Rachas: {rachas}, Z: {z:.4f}")
    
    if abs(z) < 1.96:  # 95% de confianza
        print("✅ Secuencia independiente")
    else:
        print("❌ Secuencia no independiente")
        if z > 0:
            print("   Demasiadas rachas detectadas")
        else:
            print("   Muy pocas rachas detectadas")
