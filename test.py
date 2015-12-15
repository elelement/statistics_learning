# -*- coding: utf-8 -*-
#!/usr/bin/env python

from utils.calculus import *
import math

# Ejercicios obtenidos de 'http://www.vitutor.com/pro/3/b_3.html'

def ejercicio_ejemplo():
    print f_binomial(4, 2, 0.8)

## Se lanza una moneda cuatro veces. Calcular la probabilidad de que salgan más caras que cruces
def ejercicio_1():
    # Las probabilidades de éxito (cara) y cruz (fracaso) son idénticas y valen 0.5
    # La P(X >= 3) = P(X = 3) + P(X = 4)
    p3 = f_binomial(4, 3, 0.5)
    p4 = f_binomial(4, 4, 0.5)
    print p3 + p4

## Un agente de seguros vende pólizas a cinco personas de la misma edad y que disfrutan de buena salud. 
## Según las tablas actuales, la probabilidad de que una persona en estas condiciones viva 30 años o 
## más es 2/3. Hállese la probabilidad de que, transcurridos 30 años, vivan:
def ejercicio_2():
    # Las cinco personas
    print f_binomial(5, 5, 2.0/3)

    # Al menos tres personas
    print f_binomial(5, 3, 2.0/3) + f_binomial(5, 4, 2.0/3) + f_binomial(5, 5, 2.0/3)

    # Exactamente dos personas
    print f_binomial(5, 2, 2.0/3)

## Si de seis a siete de la tarde se admite que un número de teléfono de cada cinco está comunicando, 
## ¿cuál es la probabilidad de que, cuando se marquen 10 números de teléfono elegidos al azar, sólo 
## comuniquen dos?
def ejercicio_3():
    print f_binomial(10, 2, 1.0/5)

## La probabilidad de que un hombre acierte en el blanco es 1/4. Si dispara 10 veces ¿cuál es la 
## probabilidad de que acierte exactamente en tres ocasiones? ¿Cuál es la probabilidad de que acierte 
## por lo menos en una ocasión?
def ejercicio_4():
    # En tres ocasiones:
    print f_binomial(10, 3, 1.0/4)
    # En al menos una ocasión:
    print f_binomial(10, 1, 1.0/4) + f_binomial(10, 2, 1.0/4) + f_binomial(10, 3, 1.0/4) + f_binomial(10, 4, 1.0/4) + \
          f_binomial(10, 5, 1.0/4) + f_binomial(10, 6, 1.0/4) + f_binomial(10, 7, 1.0/4) + f_binomial(10, 8, 1.0/4) + \
          f_binomial(10, 9, 1.0/4) + f_binomial(10, 10, 1.0/4)


def main():
    print "Ejemplo:"
    ejercicio_ejemplo()
    print "\nEjercicio 1:"
    ejercicio_1()
    print "\nEjercicio 2:"
    ejercicio_2()
    print "\nEjercicio 3:"
    ejercicio_3()
    print "\nEjercicio 4:"
    ejercicio_4()

if __name__ == "__main__":
    main()