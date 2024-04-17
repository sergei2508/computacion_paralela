import threading
import time

sem = threading.Semaphore(2)  # Solo permitir 2 hilos a la vez
counter = 0

def incrementar():
    global counter
    sem.acquire()
    print("se bloqueo")
    counter += 1
    sem.release()
    print("se desbloqueo")

# Crear e iniciar varios hilos
hilos = []
for _ in range(10):
    hilo = threading.Thread(target=incrementar)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print(f"Valor final del contador: {counter}")