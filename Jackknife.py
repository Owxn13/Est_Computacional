import pandas as pd
import numpy as np

archivo_csv = pd.read_csv(r'D:\Trabajos y Prácticas\V Semestre\Estadística Computacional\Datos.csv')

def jackknife(data, n_iteraciones=50):
    n = len(data)
    medias = []

    for _ in range(n_iteraciones):
        i = np.random.randint(0, n)
        muestra = np.delete(data, i)
        medias.append(np.mean(muestra))
    
    media_global = np.mean(medias)
    
    varianza_jackknife = ((n - 1) / n) * np.sum((medias - media_global) ** 2)
    
    return media_global, varianza_jackknife

media1, varianza1 = jackknife(archivo_csv["TransactionAmount"].dropna().values, n_iteraciones=50)
print("Ejercicio 1:")
print(f"Media Jackknife: {media1}")
print(f"Varianza Jackknife: {varianza1}")

media2, varianza2 = jackknife(archivo_csv["CustomerAge"].dropna().values, n_iteraciones=50)
print("\nEjercicio 2:")
print(f"Media Jackknife: {media2}")
print(f"Varianza Jackknife: {varianza2}")

media3, varianza3 = jackknife(archivo_csv["AccountBalance"].dropna().values, n_iteraciones=50)
print("\nEjercicio 3:")
print(f"Media Jackknife: {media3}")
print(f"Varianza Jackknife: {varianza3}")

media4, varianza4 = jackknife(archivo_csv["TransactionDuration"].dropna().values, n_iteraciones=50)
print("\nEjercicio 4:")
print(f"Media Jackknife: {media4}")
print(f"Varianza Jackknife: {varianza4}")

media5, varianza5 = jackknife(archivo_csv["LoginAttempts"].dropna().values, n_iteraciones=50)
print("\nEjercicio 5:")
print(f"Media Jackknife: {media5}")
print(f"Varianza Jackknife: {varianza5}")