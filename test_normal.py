# -*- coding: utf-8 -*-
#!/usr/bin/env python

from utils.calculus import *
from utils.distributions import *
import math
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
    sigma = 3.0

    # Entre 60 kg y 75 kg
    # Tipificamos las variables
    # Ojo! Una distribución normal estándar se expresa mediante N(µ, σ) = N(0, 1)
    #
    # p[60 < X <= 75] = p(z1 < Z <= z2)
    z1 = f_typify(mu, sigma, 60.0)
    z2 = f_typify(mu, sigma, 75.0)
    
    # Siguiendo la tabla p(Z > z1) = 1 - p(Z <= z1) = 1 - p(1.67)
    p1 = 1 - 0.9525

    # Siguiendo la tabla p(Z <= z2) = p(3.33)
    p2 = 0.9996

    print "Ejercicio 4:"
    print (p2 - p1) * 500

    z3 = f_typify(mu, sigma, 90)
    #print z3


if __name__ == "__main__":
    main()