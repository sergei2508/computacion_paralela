import multiprocessing

def calcular_cuadrado(numero):
    return numero * numero

if __name__ == "__main__":
    # Lista de números para calcular sus cuadrados
    numeros = [1, 2, 3, 4, 5]

    # Crear un grupo de procesos
    pool = multiprocessing.Pool()

    # Calcular los cuadrados de los números utilizando map
    resultados = pool.map(calcular_cuadrado, numeros)

    # Cerrar el grupo de procesos
    pool.close()
    pool.join()

    print("Resultados:", resultados)
