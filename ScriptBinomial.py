import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

cien = binom.rvs(100, 0.35, size =100) # Devuelve un listado del numero de exitos en 100 intentos con una probabilidad de 0.35 con distribucion binomial.
mil = binom.rvs(100, 0.35, size =1000) # Devuelve un listado del numero de exitos en 1000 intentos con una probabilidad de 0.35.
diezmil = binom.rvs(100, 0.35, size =10000) # Devuelve un listado del numero de exitos en 10000 intentos con una probabilidad de 0.35.
cienmil = binom.rvs(100, 0.35, size =100000) # Devuelve un listado del numero de exitos en 100000 intentos con una probabilidad de 0.35.


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

# Path: ScriptPoisson.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

cien = poisson.rvs(35, size =100) # Devuelve un listado del numero de exitos en 100 intentos con una probabilidad de 0.35 con distribucion binomial.
mil = poisson.rvs(35, size =1000) # Devuelve un listado del numero de exitos en 1000 intentos con una probabilidad de 0.35.
diezmil = poisson.rvs(35, size =10000) # Devuelve un listado del numero de exitos en 10000 intentos con una probabilidad de 0.35.
cienmil = poisson.rvs(35, size =100000) # Devuelve un listado del numero de exitos en 100000 intentos con una probabilidad de 0.35.


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
