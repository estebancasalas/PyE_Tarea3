import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import statistics
import seaborn as sns

#Ejercicio 1 parte a Generar muestras 

cien = binom.rvs(100, 0.35, size =100) # Devuelve un listado del numero de exitos en 100 intentos con una probabilidad de 0.35 con distribucion binomial.
mil = binom.rvs(100, 0.35, size =1000) # Devuelve un listado del numero de exitos en 1000 intentos con una probabilidad de 0.35.
diezmil = binom.rvs(100, 0.35, size =10000) # Devuelve un listado del numero de exitos en 10000 intentos con una probabilidad de 0.35.
cienmil = binom.rvs(100, 0.35, size =100000) # Devuelve un listado del numero de exitos en 100000 intentos con una probabilidad de 0.35.

var_empirical = np.var(cienmil, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cienmil)
print("Varianza teórica:", var_theoretical)

#Ejercicio 1 parte e
# falta comparacion con emperanza teorica
mediaCien = statistics.mean(cien)
mediaMil = statistics.mean(mil)
mediaDiezmil = statistics.mean(diezmil)
mediaCienmil = statistics.mean(cienmil)



#Ejercicio 1 parte d
medianaCien =  statistics.median(cien)
medianaMil= statistics.median(mil)
medianaDiezmil = statistics.median(diezmil)
medianaCienmil = statistics.median(cienmil)

modaCien = statistics.mode(cien)
modaMil = statistics.mode(mil)
modaDiezmil = statistics.mode(diezmil)
modaCienmil = statistics.mode(cienmil)

#ejercicio 1 parte c
plt.hist(cien, color="blue")
plt.show()

plt.hist(mil, color="red")
plt.show()

plt.hist(diezmil, color="yellow")
plt.show()

plt.hist(cienmil, color="pink")
plt.show()

#EJercicio 1 parte b
sns.boxplot(cien)
sns.boxplot(mil)
sns.boxplot(diezmil)
sns.boxplot(cienmil)
plt.show()

#parte f varianza empirica vs varianza teorica


# x = np.arange(0, 100) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, cien, color = 'blue') # Grafica un histograma de barras con los valores de cien.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 1000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, mil, color = 'blue') # Grafica un histograma de barras con los valores de mil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 10000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, diezmil, color = 'blue') # Grafica un histograma de barras con los valores de diezmil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 100000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, cienmil, color = 'blue') # Grafica un histograma de barras con los valores de cienmil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# # Path: ScriptPoisson.py
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import poisson

# cien = poisson.rvs(35, size =100) # Devuelve un listado del numero de exitos en 100 intentos con una probabilidad de 0.35 con distribucion binomial.
# mil = poisson.rvs(35, size =1000) # Devuelve un listado del numero de exitos en 1000 intentos con una probabilidad de 0.35.
# diezmil = poisson.rvs(35, size =10000) # Devuelve un listado del numero de exitos en 10000 intentos con una probabilidad de 0.35.
# cienmil = poisson.rvs(35, size =100000) # Devuelve un listado del numero de exitos en 100000 intentos con una probabilidad de 0.35.
#Ejercicio 1 parte d
medianaCien =  statistics.median(cien)
medianaMil= statistics.median(mil)
medianaDiezmil = statistics.median(diezmil)
medianaCienmil = statistics.median(cienmil)

modaCien = statistics.mode(cien)
modaMil = statistics.mode(mil)
modaDiezmil = statistics.mode(diezmil)
modaCienmil = statistics.mode(cienmil)

#ejercicio 1 parte c
plt.hist(cien, color="blue")
plt.show()

plt.hist(mil, color="red")
plt.show()

plt.hist(diezmil, color="yellow")
plt.show()

plt.hist(cienmil, color="pink")
plt.show()

#EJercicio 1 parte b
sns.boxplot(cien)
sns.boxplot(mil)
sns.boxplot(diezmil)
sns.boxplot(cienmil)
plt.show()

# x = np.arange(0, 100) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, cien, color = 'blue') # Grafica un histograma de barras con los valores de cien.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 1000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, mil, color = 'blue') # Grafica un histograma de barras con los valores de mil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 10000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, diezmil, color = 'blue') # Grafica un histograma de barras con los valores de diezmil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.

# x = np.arange(0, 100000) # Devuelve un listado de numeros enteros desde 0 hasta 4.
# plt.bar(x, cienmil, color = 'blue') # Grafica un histograma de barras con los valores de cienmil.
# plt.xlabel('Numero de exitos') # Etiqueta el eje x.
# plt.ylabel('Frecuencia') # Etiqueta el eje y.
# plt.show() # Muestra la grafica.


cienGeom= geom.rvs(100,0.35,size = 100)
milGeom = geom.rvs(1000, 0.35, size= 1000)
diezMilGeom = geom.rvs(10000,0.35, size= 10000)
cienMilGeom = geom.rvs(100000, 0.35, size=100000)

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

#Ejercicio 1 parte e
# falta comparacion con emperanza teorica
mediaCien = statistics.mean(cienGeom)
mediaMil = statistics.mean(milGeom)
mediaDiezmil = statistics.mean(diezMilGeom)
mediaCienmil = statistics.mean(cienMilGeom)



#Ejercicio 1 parte d
medianaCien =  statistics.median(cienGeom)
medianaMil= statistics.median(milGeom)
medianaDiezmil = statistics.median(diezMilGeom)
medianaCienmil = statistics.median(cienMilGeom)

modaCien = statistics.mode(cienGeom)
modaMil = statistics.mode(milGeom)
modaDiezmil = statistics.mode(diezMilGeom)
modaCienmil = statistics.mode(cienMilGeom)

#ejercicio 1 parte c
plt.hist(cienGeom, color="blue")
plt.show()

plt.hist(milGeom, color="red")
plt.show()

plt.hist(diezMilGeom, color="yellow")
plt.show()

plt.hist(cienMilGeom, color="pink")
plt.show()

#EJercicio 1 parte b
sns.boxplot(cienGeom)
sns.boxplot(milGeom)
sns.boxplot(diezMilGeom)
sns.boxplot(cienMilGeom)
plt.show()