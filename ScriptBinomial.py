import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import statistics
import seaborn as sns

#Ejercicio 1 parte a Generar muestras 

#Muestra 100
print("Muestra 100: \n ------------------------------------------")
cien = binom.rvs(100, 0.35, size =100) # Devuelve un listado del numero de exitos en 100 intentos con una probabilidad de 0.35 con distribucion binomial.
#parte b
sns.boxplot(cien)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(cien, color="blue")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#parte d
medianaCien =  statistics.median(cien)
print("Mediana:", medianaCien)

modaCien = statistics.mode(cien)
print("Moda:", modaCien)

#parte e
mediaCien = statistics.mean(cien)
print("Media:", mediaCien)

#parte f
var_empirical = np.var(cien, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cien)
print("Varianza teórica:", var_theoretical)

print("\n")
#Muestra 1000
print("Muestra 1000: \n ------------------------------------------")
mil = binom.rvs(100, 0.35, size =1000) # Devuelve un listado del numero de exitos en 1000 intentos con una probabilidad de 0.35.

#parte b
sns.boxplot(mil)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(mil, color="red")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#parte d
medianaMil= statistics.median(mil)
print("Mediana de mil:", medianaMil)

modaMil = statistics.mode(mil)
print("Moda de mil:", modaMil)

#parte e
mediaMil = statistics.mean(mil)
print("Media de mil:", mediaMil)

#parte f
var_empirical = np.var(mil, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(mil)
print("Varianza teórica:", var_theoretical)

print("\n")
#Muestra 10000
print("Muestra 10.000: \n ------------------------------------------")
diezmil = binom.rvs(100, 0.35, size =10000) # Devuelve un listado del numero de exitos en 10000 intentos con una probabilidad de 0.35.

#parte b
sns.boxplot(diezmil)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(diezmil, color="yellow")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#parte d
medianaDiezmil = statistics.median(diezmil)
print("Mediana de diezmil:", medianaDiezmil)

modaDiezmil = statistics.mode(diezmil)
print("Moda de diezmil:", modaDiezmil)

#parte e
mediaDiezmil = statistics.mean(diezmil)
print("Media de diezmil:", mediaDiezmil)

#parte f
var_empirical = np.var(diezmil, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(diezmil)
print("Varianza teórica:", var_theoretical)

print("\n\n")
#Muestra 100000
print("Muestra 100.000: \n ------------------------------------------")
cienmil = binom.rvs(100, 0.35, size =100000) # Devuelve un listado del numero de exitos en 100000 intentos con una probabilidad de 0.35.

#parte b
sns.boxplot(cienmil)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#parte c
plt.hist(cienmil, color="pink")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

#parte d

medianaCienmil = statistics.median(cienmil)
print("Mediana de cienmil:", medianaCienmil)

modaCienmil = statistics.mode(cienmil)
print("Moda de cienmil:", modaCienmil)


#parte e
# falta comparacion con emperanza teorica
mediaCienmil = statistics.mean(cienmil)
print("Media de cienmil:", mediaCienmil)


#parte f varianza empirica vs varianza teorica
var_empirical = np.var(cienmil, ddof=1)
print("Varianza empírica:", var_empirical)

var_theoretical = np.var(cienmil)
print("Varianza teórica:", var_theoretical)

print("\n")

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
