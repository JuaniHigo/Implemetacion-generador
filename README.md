# Implementación y Análisis de Generadores Pseudoaleatorios

Este proyecto se enfoca en la implementación y evaluación de algoritmos clásicos para la generación de números pseudoaleatorios (PRNGs). El objetivo principal es construir estos generadores desde cero y luego someter las secuencias de números resultantes a un conjunto de pruebas estadísticas para evaluar su calidad, es decir, qué tan bien se aproximan a una secuencia verdaderamente aleatoria (uniforme e independiente).

---

## 📂 Estructura del Repositorio

El proyecto está compuesto por un módulo central de pruebas y varios scripts que implementan diferentes generadores.

### Módulo de Pruebas

* `testsGeneradores.py`: Este es un módulo compartido que contiene 4 pruebas estadísticas fundamentales para analizar la aleatoriedad de una secuencia de números. Es importado por cada uno de los scripts generadores.

### Scripts Generadores

Cada uno de estos scripts implementa un método de generación diferente, produce una secuencia de números y luego utiliza el módulo `testsGeneradores.py` para evaluarla.

* `randomGLC.py`: Implementa el **Generador Lineal Congruencial (LCG)**, un método clásico basado en la fórmula `Xn+1 = (a * Xn + c) mod m`.
* `randomMidSquare.py`: Implementa el **Método de los Cuadrados Medios**, uno de los primeros algoritmos de PRNG, propuesto por John von Neumann.
* `randomPython.py`: Utiliza el generador nativo de Python (`random.seed` y `random.randint`) como punto de referencia para comparar la calidad de los otros métodos.

---

## 🎲 Pruebas de Aleatoriedad Implementadas

El módulo `testsGeneradores.py` incluye las siguientes validaciones:

1.  **Test de Frecuencia (Chi-Cuadrado):** Evalúa si los dígitos (0-9) en los números generados aparecen con la misma frecuencia, es decir, si siguen una distribución uniforme.
2.  **Test Chi-Cuadrado (para uniformidad):** Comprueba si los números generados se distribuyen de manera uniforme a lo largo de todo su rango de valores.
3.  **Test de Póker:** Analiza la frecuencia de patrones de dígitos (como pares, tríos, etc.) para detectar dependencias entre ellos.
4.  **Test de Rachas:** Evalúa la independencia de la secuencia analizando el número de rachas ascendentes y descendentes.

---

## 📄 Informe del Proyecto

Para una explicación detallada de los métodos, el fundamento matemático de las pruebas y un análisis completo de los resultados obtenidos, podés consultar el **[informe completo en PDF](TP_2_1_Generadores_Pseudoaleatorios.pdf)**.


## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **NumPy:** Para operaciones numéricas eficientes.
* **SciPy:** Utilizado en las pruebas estadísticas, específicamente para la función `chisquare`.
* **Matplotlib:** Para la visualización de la distribución de los valores generados.

---

## 🚀 Cómo Ejecutar

Cada generador se puede ejecutar de forma independiente desde la terminal. Los parámetros como la semilla y la cantidad de números se pasan como argumentos de línea de comandos.

```bash
# Ejemplo de ejecución para el Generador Lineal Congruencial
python randomGLC.py -s 1234 -a 1664525 -c 1013904223 -m 4294967296 -n 1000

# Ejemplo de ejecución para el Método de Cuadrados Medios
python randomMidSquare.py -s 5735 -n 100

# Ejemplo de ejecución para el generador de Python
python randomPython.py -s 123 -n 1000
```
