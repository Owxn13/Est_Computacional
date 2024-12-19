import pandas as pd
import numpy as np

archivo_csv = pd.read_csv(r'D:\Trabajos y Prácticas\V Semestre\Estadística Computacional\Datos.csv')

def bootstrap(data, n_iteraciones=50):
    medias = []
    desviaciones = []
    
    for i in range(n_iteraciones):
        muestra = np.random.choice(data, size=len(data), replace=True)
        medias.append(np.mean(muestra))
        desviaciones.append(np.std(muestra))
        
    intervalo = np.percentile(medias, [2.5, 97.5])
    media_final = np.mean(medias)
    desviacion_final = np.mean(desviaciones)
    
    return intervalo, media_final, desviacion_final

intervalo1, media1, desviacion1 = bootstrap(archivo_csv["TransactionAmount"])
print("Ejercicio 1:")
print("Intervalo de confianza: ", intervalo1)
print("Media final: ", media1)
print("Desviación final: ", desviacion1)

intervalo2, media2, desviacion2 = bootstrap(archivo_csv["CustomerAge"])
print("\nEjercicio 2:")
print("Intervalo de confianza: ", intervalo2)
print("Media final: ", media2)
print("Desviación final: ", desviacion2)

intervalo3, media3, desviacion3 = bootstrap(archivo_csv["TransactionDuration"])
print("\nEjercicio 3:")
print("Intervalo de confianza: ", intervalo3)
print("Media final: ", media3)
print("Desviación final: ", desviacion3)

intervalo4, media4, desviacion4 = bootstrap(archivo_csv["AccountBalance"])
print("\nEjercicio 4:")
print("Intervalo de confianza: ", intervalo4)
print("Media final: ", media4)
print("Desviación final: ", desviacion4)

intervalo5, media5, desviacion5 = bootstrap(archivo_csv["LoginAttempts"])
print("\nEjercicio 5:")
print("Intervalo de confianza: ", intervalo5)
print("Media final: ", media5)
print("Desviación final: ", desviacion5)




















































import pandas as pd
import numpy as np

def bootstrap(data, n_iteraciones=50):
    muestras = [np.random.choice(data, size=len(data), replace=True) for _ in range(n_iteraciones)]
    medias = [np.mean(m) for m in muestras]
    desviaciones = [np.std(m) for m in muestras]
    return np.percentile(medias, [2.5, 97.5]), np.mean(medias), np.mean(desviaciones)

data = pd.read_csv(r'D:\Trabajos y Prácticas\V Semestre\Estadística Computacional\Datos.csv')
columnas = ["TransactionAmount", "CustomerAge", "TransactionDuration", "AccountBalance", "LoginAttempts"]

for i, col in enumerate(columnas, 1):
    intervalo, media, desviacion = bootstrap(data[col])
    print(f"\nEjercicio {i}:")
    print(f"Intervalo de confianza: {intervalo}")
    print(f"Media final: {media}")
    print(f"Desviación final: {desviacion}")