# Path: ScriptPoisson.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import statistics
import seaborn as sns

cien = poisson.rvs(30, size =100) # Devuelve un listado del numero de exitos en 100 intentos con una probabilidad de 0.35 con distribucion binomial.
mil = poisson.rvs(30, size =1000) # Devuelve un listado del numero de exitos en 1000 intentos con una probabilidad de 0.35.
diezmil = poisson.rvs(30, size =10000) # Devuelve un listado del numero de exitos en 10000 intentos con una probabilidad de 0.35.
cienmil = poisson.rvs(30, size =100000) # Devuelve un listado del numero de exitos en 100000 intentos con una probabilidad de 0.35.

#Ejercicio 1 parte b
sns.boxplot(cien)
sns.boxplot(mil)
sns.boxplot(diezmil)
sns.boxplot(cienmil)
plt.show()

#ejercicio 1 parte c
plt.hist(cien, color="blue")
plt.show()

plt.hist(mil, color="red")
plt.show()

plt.hist(diezmil, color="yellow")
plt.show()

plt.hist(cienmil, color="pink")
plt.show()

#Ejercicio 1 parte d
medianaCien =  statistics.median(cien)
medianaMil= statistics.median(mil)
medianaDiezmil = statistics.median(diezmil)
medianaCienmil = statistics.median(cienmil)

modaCien = statistics.mode(cien)
modaMil = statistics.mode(mil)
modaDiezmil = statistics.mode(diezmil)
modaCienmil = statistics.mode(cienmil)


#Ejercicio 1 parte e
# falta comparacion con emperanza teorica
mediaCien = statistics.mean(cien)
mediaMil = statistics.mean(mil)
mediaDiezmil = statistics.mean(diezmil)
mediaCienmil = statistics.mean(cienmil)

#Parte f
var_empirical = np.var(cien, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cien)
print("Varianza teórica:", var_theoretical)


var_empirical = np.var(mil, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(mil)
print("Varianza teórica:", var_theoretical)


var_empirical = np.var(diezmil, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(diezmil)
print("Varianza teórica:", var_theoretical)


var_empirical = np.var(cienmil, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cienmil)
print("Varianza teórica:", var_theoretical)
x = np.arange(0, 100) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, cien, color = 'blue') # Grafica un histograma de barras con los valores de cien.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.

x = np.arange(0, 1000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, mil, color = 'blue') # Grafica un histograma de barras con los valores de mil.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.

x = np.arange(0, 10000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, diezmil, color = 'blue') # Grafica un histograma de barras con los valores de diezmil.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.

x = np.arange(0, 100000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, cienmil, color = 'blue') # Grafica un histograma de barras con los valores de cienmil.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.

