__author__ = 'jmcabrera'

from calculus import *
import concurrent.futures

def binomial(n, p):
    bX = []
    bY = []
    aux = 0
    for x in xrange(0, n):
        aux += f_binomial(n, x, p)
        bX.append(x)
        bY.append(aux)
    return (bX, bY) # Devolvemos una tupla con las dos listas

def binomial_p(n, p, workers):
    futureQ = []
    bX = []
    bY = []
    aux = 0
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
    for x in xrange(0, n):
        bX.append(x)
        futureQ.append(executor.submit(f_binomial, n, x, p))

    for future in futureQ:
        try:
            aux += future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (x, exc))
            raise
        else:
            bY.append(aux)

    return (bX, bY) # Devolvemos una tupla con las dos listas

def probability(n, p):
    bX = []
    bY = []
    for x in xrange(0, n):
        bX.append(x)
        bY.append(f_binomial(n, x, p))
        
    return (bX, bY)

def normal(n, mu, sigma):
    bX = []
    bY = []
    for x in n:
        bX.append(x)
        bY.append(f_gauss(mu, sigma, x))
    return (bX, bY) # Devolvemos una tupla con las dos listas