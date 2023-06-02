import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
import statistics
import seaborn as sns


cienGeom= geom.rvs(0.08,size= 100)
milGeom = geom.rvs( 0.08, size= 1000)
diezMilGeom = geom.rvs(0.08, size= 10000)
cienMilGeom = geom.rvs( 0.08, size=100000)

#EJercicio 1 parte b
sns.boxplot(cienGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()
sns.boxplot(milGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()
sns.boxplot(diezMilGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()
sns.boxplot(cienMilGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#ejercicio 1 parte c
plt.hist(cienGeom, color="blue")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

plt.hist(milGeom, color="red")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

plt.hist(diezMilGeom, color="yellow")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

plt.hist(cienMilGeom, color="pink")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#Ejercicio 1 parte d
medianaCien =  statistics.median(cienGeom)
print("Mediana de cien:", medianaCien)
medianaMil= statistics.median(milGeom)
print("Mediana de mil:", medianaMil)
medianaDiezmil = statistics.median(diezMilGeom)
print("Mediana de diezmil:", medianaDiezmil)
medianaCienmil = statistics.median(cienMilGeom)
print("Mediana de cienmil:", medianaCienmil)

modaCien = statistics.mode(cienGeom)
print("Moda de cien:", modaCien)
modaMil = statistics.mode(milGeom)
print("Moda de mil:", modaMil)
modaDiezmil = statistics.mode(diezMilGeom)
print("Moda de diezmil:", modaDiezmil)
modaCienmil = statistics.mode(cienMilGeom)
print("Moda de cienmil:", modaCienmil)

#Ejercicio 1 parte e
# falta comparacion con emperanza teorica
mediaCien = statistics.mean(cienGeom)
print("Media de cien:", mediaCien)
mediaMil = statistics.mean(milGeom)
print("Media de mil:", mediaMil)
mediaDiezmil = statistics.mean(diezMilGeom)
print("Media de diezmil:", mediaDiezmil)
mediaCienmil = statistics.mean(cienMilGeom)
print("Media de cienmil:", mediaCienmil)


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


# x = np.arange(0, 100) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, cienGeom, color = 'blue') # Grafica un histograma de barras con los valores de cien.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 1000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, milGeom, color = 'blue') # Grafica un histograma de barras con los valores de mil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 10000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, diezMilGeom, color = 'blue') # Grafica un histograma de barras con los valores de diezmil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 100000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, cienMilGeom, color = 'blue') # Grafica un histograma de barras con los valores de cienmil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.










