# -*- coding: utf-8 -*-
#!/usr/bin/env python

from utils.calculus import *
import math

# Ejercicios obtenidos de 'http://www.vitutor.com/pro/3/b_3.html'

def main():
    # En unas pruebas de alcoholemia se ha observado que el 5% de los conductores controlados 
    # dan positivo en la prueba y que el 10% de los conductores controlados no llevan puesto 
    # el cinturón de seguridad. También se ha observado que las dos infracciones son independientes. 
    # Un guardia de tráfico para cinco conductores al azar. Si tenemos en cuenta que el número de 
    # conductores es suficientemente importante como para estimar que la proporción de infractores 
    # no varía al hacer la selección.

    # 1. Determinar la probabilidad de que exactamente tres conductores hayan cometido alguna de 
    # las dos infracciones
    # La probabilidad de A U B es P(A) + P(B) - P(A)*P(B)
    p = 0.05 + 0.1 - (0.05 * 0.1)
    print p
    print "Ejercicio 1:"
    print f_binomial(5, 3, p)

    # 2. Determine la probabilidad de que al menos uno de los conductores controlados haya cometido 
    # alguna de las dos infracciones
    binCombinada = f_binomial(5, 1, p) + f_binomial(5, 2, p) + f_binomial(5, 3, p) + \
                  f_binomial(5, 4, p) + f_binomial(5, 5, p) 
    print binCombinada

    # Un laboratorio afirma que una droga causa efectos secundarios en una proporción de 3 de cada 
    # 100 pacientes. Para contrastar esta afirmación, otro laboratorio elige al azar a 5 pacientes
    # a los que aplica la droga. ¿Cuál es la probabilidad de los siguientes sucesos?
    
    print "Ejercicio 2:"

    # 1. Ningún paciente tenga efectos secundarios
    p = 0.03
    print f_binomial(5, 0, p)

    # 2. Al menos dos tengan efectos secundarios
    print f_binomial(5, 2, p) + f_binomial(5, 3, p) + f_binomial(5, 4, p) + f_binomial(5, 5, p)

    # 3. ¿Cuál es el número medio de pacientes que espera el laboratorio que sufran efectos 
    # secundarios si elige 100 pacientes al azar?
    print mean(100, p)


if __name__ == "__main__":
    main()