# Monitor de entrenamiento de IA

"""
Nombre del Alumno: Luz María Robles Barradas
Matrícula: UX25II081
Fecha: 25 MAYO 2026
Examen Segundo Parcial - Programación Estructurada
"""

# IMPORTACIÓN DE BIBLIOTECAS

import datetime
import math
import random
import statistics
import sys

# DEFINICIÓN DE CONSTANTES

MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95

# FUNCIÓN DE INFORMACIÓN DEL SISTEMA

"""
esta funcion muestra informacion basica
del sistema donde se está ejecutando
el programa, (utiliza la biblioteca sys 
para mostrar la plataforma, la versión de python
y algunos datos importantes del entorno)
"""


def obtener_info_sistema():

    print("\nINFORMACIÓN DEL SISTEMA")

    print("Plataforma:", sys.platform)

    print("Versión de Python:", sys.version)

    print("Tamaño máximo entero:", sys.maxsize)

# FUNCIÓN DE ENTRENAMIENTO

"""
esta funcion simula el proceso de
entrenamiento de un modelo de IA, durante 
cada epoch se generan valores
aleatorios de pérdida, probabilidad
de exito y eventos del entrenamiento (tambien
utiliza datetime para registrar
el tiempo de inicio y finalización
del proceso)
"""

def simular_metricas_entrenamiento():

    lista_loss = []
    lista_latencia = []

    eventos = [
        "Epoch exitoso",
        "Gradiente inestable",
        "Actualización de pesos"
    ]

    inicio = datetime.datetime.now()

    fecha = inicio.strftime("%d/%m/%Y %H:%M:%S")

    print("\nINICIO DEL ENTRENAMIENTO")
    print("Fecha:", fecha)

    for epoch in range(1, MAX_EPOCHS + 1):

        print("\nEpoch:", epoch)

        loss = random.uniform(0.10, 1.00)

        probabilidad = random.random()

        evento = random.choice(eventos)

        latencia = random.uniform(0.2, 1.5)

        lista_loss.append(loss)
        lista_latencia.append(latencia)

        print("Loss:", round(loss, 4))
        print("Probabilidad:", round(probabilidad, 4))
        print("Evento:", evento)
        print("Latencia:", round(latencia, 4))

        match evento:

            case "Epoch exitoso":
                print("El modelo aprendió correctamente")

            case "Gradiente inestable":
                print("Existe inestabilidad en el entrenamiento")

            case "Actualización de pesos":
                print("Los pesos fueron actualizados")

            case _:
                print("Evento desconocido")

        if loss >= UMBRAL_ERROR_CRITICO:

            print("\nERROR CRÍTICO DETECTADO")
            print("Entrenamiento detenido")

            sys.exit()

    fin = datetime.datetime.now()

    diferencia = fin - inicio

    print("\nFIN DEL ENTRENAMIENTO")
    print("Tiempo total:", diferencia)

    return lista_loss, lista_latencia

# FUNCIÓN DE ANÁLISIS

"""
esta función analiza los resultados
obtenidos durante el entrenamiento
(con ayuda de la biblioteca statistics
se calcula el promedio de pérdida,
la desviación estándar y la mediana
de la latencia)
"""

def analizar_rendimiento(lista_loss, lista_latencia):

    print("\nANÁLISIS DE RENDIMIENTO")

    promedio = statistics.mean(lista_loss)

    desviacion = statistics.stdev(lista_loss)

    mediana = statistics.median(lista_latencia)

    print("Promedio de loss:", round(promedio, 4))
    print("Desviación estándar:", round(desviacion, 4))
    print("Mediana de latencia:", round(mediana, 4))

# FUNCIÓN RMSE

"""
esta función calcula el RMSE
(Root Mean Squared Error), se comparan 
valores reales y
predicciones utilizando operaciones
matemáticas de la biblioteca math
como valor absoluto, potencia
y raíz cuadrada.
"""

def calcular_rmse():

    predicciones = [0.9, 0.8, 0.7, 0.95, 0.85]
    reales = [1.0, 0.75, 0.65, 1.0, 0.80]

    suma = 0

    for i in range(len(predicciones)):

        diferencia = predicciones[i] - reales[i]

        absoluto = math.fabs(diferencia)

        cuadrado = math.pow(absoluto, 2)

        suma = suma + cuadrado

    promedio = suma / len(predicciones)

    rmse = math.sqrt(promedio)

    epochs = math.ceil(rmse * 10)

    print("\nRESULTADOS RMSE")
    print("RMSE:", round(rmse, 4))
    print("Epochs estimados:", epochs)


"""
esta función principal controla
el flujo completo del programa.
(se encarga de llamar las demás
funciones necesarias para ejecutar
la simulación del entrenamiento,
analizar resultados y calcular
las métricas finales)
"""


def main():

    print("SIMULADOR DE ENTRENAMIENTO IA")

    obtener_info_sistema()

    losses, latencias = simular_metricas_entrenamiento()

    analizar_rendimiento(losses, latencias)

    calcular_rmse()

    print("\nPrograma finalizado correctamente")

# EJECUCIÓN DEL PROGRAMA

if __name__ == "__main__":
    main()



"""
1. En datetime.datetime.now(), datetime es la
clase que pertenece a la biblioteca datetime
y now() es el método utilizado para obtener
la fecha y hora actual del sistema.
"""

"""
2. Cuando se utiliza import math es necesario
escribir math.sqrt() para acceder a la función.
En cambio, con from math import sqrt solo se
escribe sqrt() directamente.
"""

"""
3. Primero la función de simulación genera los
datos aleatorios del entrenamiento y los guarda
en listas. Después esos datos son enviados a
las funciones de análisis y cálculo de RMSE.
"""

"""
4. Se utilizaron listas como lista_loss y
lista_latencia porque permiten almacenar
múltiples valores relacionados con el
entrenamiento y recorrerlos fácilmente.
"""

"""
5. No fue necesario programar manualmente la
fórmula de la desviación estándar, ya que
la biblioteca statistics incluye la función
stdev() para realizar ese cálculo.
"""

