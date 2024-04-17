import multiprocessing
import time

def tarea_intensiva(valor):
    # Simular una tarea intensiva
    resultado = valor * valor
    time.sleep(1)  # Simular una espera de 1 segundo
    return resultado

def cluster_procesos():
    # Crear un grupo de procesos con el máximo de procesos disponibles
    pool = multiprocessing.Pool()

    # Lista de valores para la tarea intensiva
    valores = [1, 2, 3, 4, 5]

    # Aplicar la tarea intensiva en paralelo a los valores
    resultados = pool.map(tarea_intensiva, valores)

    # Cerrar el grupo de procesos
    pool.close()
    pool.join()

    return resultados

def proceso_individual():
    # Lista de valores para la tarea intensiva
    valores = [1, 2, 3, 4, 5]

    # Aplicar la tarea intensiva secuencialmente
    resultados = [tarea_intensiva(valor) for valor in valores]

    return resultados

if __name__ == "__main__":
    # Usar un cluster de procesos
    start_time_cluster = time.time()
    resultados_cluster = cluster_procesos()
    end_time_cluster = time.time()
    tiempo_cluster = end_time_cluster - start_time_cluster

    # Usar un solo proceso
    start_time_proceso = time.time()
    resultados_proceso = proceso_individual()
    end_time_proceso = time.time()
    tiempo_proceso = end_time_proceso - start_time_proceso

    print("Resultados usando cluster de procesos:", resultados_cluster)
    print(f"Tiempo usando cluster de procesos: {tiempo_cluster} segundos")

    print("Resultados usando un solo proceso:", resultados_proceso)
    print(f"Tiempo usando un solo proceso: {tiempo_proceso} segundos")
