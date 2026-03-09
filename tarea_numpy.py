import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

N = 10_000_000
NUM_HILOS = 8
# ------------------------------------

def mi_suma(datos):
    # Usamos la suma de numpy dentro del hilo para que sea veloz
    return np.sum(datos)

def main():
    # 1. Generar datos
    datos = np.random.randint(0, 10, N, dtype=np.int64)
    
    # 2. Dividir el arreglo en trozos según el número de hilos
    lista_de_trozos = np.array_split(datos, NUM_HILOS)
    
    inicio = time.time()

    # 3. Ejecutar la suma en hilos
    with ThreadPoolExecutor(max_workers=NUM_HILOS) as executor:
        resultados = list(executor.map(mi_suma, lista_de_trozos))

    # 4. Sumar los resultados parciales obtenidos de cada hilo
    suma_final = sum(resultados)
    
    fin = time.time()

    print(f"Número de hilos = {NUM_HILOS}")
    print(f"Suma total = {suma_final}")
    print(f"Tiempo de ejecución = {fin - inicio:.6f} segundos")

main()