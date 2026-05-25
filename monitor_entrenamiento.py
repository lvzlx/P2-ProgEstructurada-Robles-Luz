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

def analizar_rendimiento(lista_loss, lista_latencia):

    print("\nANÁLISIS DE RENDIMIENTO")

    promedio = statistics.mean(lista_loss)

    desviacion = statistics.stdev(lista_loss)

    mediana = statistics.median(lista_latencia)

    print("Promedio de loss:", round(promedio, 4))
    print("Desviación estándar:", round(desviacion, 4))
    print("Mediana de latencia:", round(mediana, 4))

# FUNCIÓN RMSE

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



