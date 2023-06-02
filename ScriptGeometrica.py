import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
import statistics
import seaborn as sns


cienGeom= geom.rvs(100,0.35,size = 100)
milGeom = geom.rvs(1000, 0.35, size= 1000)
diezMilGeom = geom.rvs(10000,0.35, size= 10000)
cienMilGeom = geom.rvs(100000, 0.35, size=100000)

#EJercicio 1 parte b
sns.boxplot(cienGeom)
sns.boxplot(milGeom)
sns.boxplot(diezMilGeom)
sns.boxplot(cienMilGeom)
plt.show()

#ejercicio 1 parte c
plt.hist(cienGeom, color="blue")
plt.show()

plt.hist(milGeom, color="red")
plt.show()

plt.hist(diezMilGeom, color="yellow")
plt.show()

plt.hist(cienMilGeom, color="pink")
plt.show()

#Ejercicio 1 parte d
medianaCien =  statistics.median(cienGeom)
medianaMil= statistics.median(milGeom)
medianaDiezmil = statistics.median(diezMilGeom)
medianaCienmil = statistics.median(cienMilGeom)

modaCien = statistics.mode(cienGeom)
modaMil = statistics.mode(milGeom)
modaDiezmil = statistics.mode(diezMilGeom)
modaCienmil = statistics.mode(cienMilGeom)

#Ejercicio 1 parte e
# falta comparacion con emperanza teorica
mediaCien = statistics.mean(cienGeom)
mediaMil = statistics.mean(milGeom)
mediaDiezmil = statistics.mean(diezMilGeom)
mediaCienmil = statistics.mean(cienMilGeom)


#Parte f
var_empirical = np.var(cienGeom, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cienGeom)
print("Varianza teórica:", var_theoretical)

var_empirical = np.var(milGeom, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(milGeom)
print("Varianza teórica:", var_theoretical)

var_empirical = np.var(diezMilGeom, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(diezMilGeom)
print("Varianza teórica:", var_theoretical)

var_empirical = np.var(cienMilGeom, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cienMilGeom)
print("Varianza teórica:", var_theoretical)

x = np.arange(0, 100) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, cienGeom, color = 'blue') # Grafica un histograma de barras con los valores de cien.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.

x = np.arange(0, 1000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, milGeom, color = 'blue') # Grafica un histograma de barras con los valores de mil.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.

x = np.arange(0, 10000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, diezMilGeom, color = 'blue') # Grafica un histograma de barras con los valores de diezmil.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.

x = np.arange(0, 100000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
plt.bar(x, cienMilGeom, color = 'blue') # Grafica un histograma de barras con los valores de cienmil.
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show() # Muestra la grafica.










