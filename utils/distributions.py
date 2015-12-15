__author__ = 'jmcabrera'

from calculus import *

def binomial(n, p):
    bX = []
    bY = []
    aux = 0
    for x in xrange(0, n):
        aux += f_binomial(n, x, p)
        bX.append(x)
        bY.append(aux)
    return (bX, bY) # Devolvemos una tupla con las dos listas

def probability(n, p):
    bX = []
    bY = []
    for x in xrange(0, n):
        bX.append(x)
        bY.append(f_binomial(n, x, p))
        
    return (bX, bY)