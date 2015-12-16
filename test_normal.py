# -*- coding: utf-8 -*-
#!/usr/bin/env python

from utils.calculus import *
from utils.distributions import *
import math
import matplotlib.pyplot as plt
import time

# Ejercicios obtenidos de 'http://www.vitutor.com/pro/3/b_3.html'

def main():
    ## Ejercicio 1
    # Si X es una variable aleatoria de una distribución N(µ, σ), hallar: p(µ−3σ ≤ X ≤ µ+3σ)


    ## Ejercicio 4
    # La media de los pesos de 500 estudiantes de un colegio es 70 kg y la desviación típica 
    # 3 kg. Suponiendo que los pesos se distribuyen normalmente, hallar cuántos estudiantes pesan:
    bX = []
    bY = []
    total = 500
    mu = 70.0
    sigma = 3.

    # Entre 60 kg y 75 kg
    # p[60 < Z <= 75] = p()
    z1 = f_typify(mu, sigma, 60.0)
    z2 = f_typify(mu, sigma, 75.0)


    print z1
    print z2
    start = time.time()
    bX, bY = normal(total, 70, 3)
    end = time.time()
    print "Tiempo total de cálculo:"
    print end - start

    # Φ(k) = P(z ≤ k)


    # Y, finalmente, pintamos las gráficas
    plt.plot(bX, bY)
    plt.show()

if __name__ == "__main__":
    main()