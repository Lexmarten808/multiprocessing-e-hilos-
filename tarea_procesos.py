import multiprocessing
import time
import numpy as np

from multiprocessing import Pool

inicio = time.time()

def mi_suma(datos):
    suma = 0
    for i in datos:
        suma = suma +i
    return suma
if __name__ == "__main__":
    N=100000000
    num_cpus=8

    datos= np.random.randint(0,10,N)
    lista_de_trozos =np.array_split(datos,num_cpus)


    with Pool(processes=num_cpus) as pool:
        resultados = pool.map(mi_suma, lista_de_trozos)

    for i in range(10_000_000):
        pass

    fin = time.time()
    print ("numero de cpus = ", num_cpus)
    print("tiempo de ejecucion = ", fin-inicio)

    print(mi_suma(resultados))