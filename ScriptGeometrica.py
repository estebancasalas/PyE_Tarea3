import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
import statistics
import seaborn as sns

#Muestra 100
cienGeom= geom.rvs(0.08,size= 100)

#parte b
sns.boxplot(cienGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(cienGeom, color="blue")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#parte d
medianaCien =  statistics.median(cienGeom)
print("Mediana de cien:", medianaCien)

modaCien = statistics.mode(cienGeom)
print("Moda de cien:", modaCien)

#parte e
mediaCien = statistics.mean(cienGeom)
print("Media de cien:", mediaCien)

#Parte f
var_empirical = np.var(cienGeom, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cienGeom)
print("Varianza teórica:", var_theoretical)
#--------------------------------------------------------------------
#Muestra 1000
milGeom = geom.rvs( 0.08, size= 1000)

#parte b 
sns.boxplot(milGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(milGeom, color="red")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()
#parte d
medianaMil= statistics.median(milGeom)
print("Mediana de mil:", medianaMil)

modaMil = statistics.mode(milGeom)
print("Moda de mil:", modaMil)

#parte e
mediaMil = statistics.mean(milGeom)
print("Media de mil:", mediaMil)

#parte f
var_empirical = np.var(milGeom, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(milGeom)
print("Varianza teórica:", var_theoretical)
#--------------------------------------------------------------------

#Muestra 10000
diezMilGeom = geom.rvs(0.08, size= 10000)

#parte b
sns.boxplot(diezMilGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(diezMilGeom, color="yellow")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#parte d
medianaDiezmil = statistics.median(diezMilGeom)
print("Mediana de diezmil:", medianaDiezmil)

modaDiezmil = statistics.mode(diezMilGeom)
print("Moda de diezmil:", modaDiezmil)

#parte e
mediaDiezmil = statistics.mean(diezMilGeom)
print("Media de diezmil:", mediaDiezmil)

#parte f
var_empirical = np.var(diezMilGeom, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(diezMilGeom)
print("Varianza teórica:", var_theoretical)
#--------------------------------------------------------------------
#Muestra 100000
cienMilGeom = geom.rvs( 0.08, size=100000)

#parte b 
sns.boxplot(cienMilGeom)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(cienMilGeom, color="pink")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#parte d
medianaCienmil = statistics.median(cienMilGeom)
print("Mediana de cienmil:", medianaCienmil)

modaCienmil = statistics.mode(cienMilGeom)
print("Moda de cienmil:", modaCienmil)


# parte e
mediaCienmil = statistics.mean(cienMilGeom)
print("Media de cienmil:", mediaCienmil)


#parte f

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










