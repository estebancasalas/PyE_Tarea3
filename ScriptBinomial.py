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

#EJercicio 1 parte b
sns.boxplot(cien)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()
sns.boxplot(mil)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()
sns.boxplot(diezmil)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()
sns.boxplot(cienmil)
plt.ylabel('Numero de exitos') # Etiqueta el eje y.
plt.show()

#ejercicio 1 parte c
plt.hist(cien, color="blue")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

plt.hist(mil, color="red")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

plt.hist(diezmil, color="yellow")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()

plt.hist(cienmil, color="pink")
plt.xlabel('Numero de exitos') # Etiqueta el eje x.
plt.ylabel('Frecuencia') # Etiqueta el eje y.
plt.show()


#Ejercicio 1 parte d
medianaCien =  statistics.median(cien)
print("Mediana de cien:", medianaCien)
medianaMil= statistics.median(mil)
print("Mediana de mil:", medianaMil)
medianaDiezmil = statistics.median(diezmil)
print("Mediana de diezmil:", medianaDiezmil)
medianaCienmil = statistics.median(cienmil)
print("Mediana de cienmil:", medianaCienmil)

modaCien = statistics.mode(cien)
print("Moda de cien:", modaCien)
modaMil = statistics.mode(mil)
print("Moda de mil:", modaMil)
modaDiezmil = statistics.mode(diezmil)
print("Moda de diezmil:", modaDiezmil)
modaCienmil = statistics.mode(cienmil)
print("Moda de cienmil:", modaCienmil)

#Ejercicio 1 parte e
# falta comparacion con emperanza teorica
mediaCien = statistics.mean(cien)
print("Media de cien:", mediaCien)
mediaMil = statistics.mean(mil)
print("Media de mil:", mediaMil)
mediaDiezmil = statistics.mean(diezmil)
print("Media de diezmil:", mediaDiezmil)
mediaCienmil = statistics.mean(cienmil)
print("Media de cienmil:", mediaCienmil)


#parte f varianza empirica vs varianza teorica
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
