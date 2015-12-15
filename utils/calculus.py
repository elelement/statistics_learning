# -*- coding: utf-8 -*-
__author__ = 'jmcabrera'
__doc__ = 'http://www.vitutor.com/pro/3/b_3.html'

import math

def factorial(value):
	result = 1
	while(value > 1):
	    result *= value
	    value -= 1
	return result

def n_combinatory(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))

## Función binomial de probabilidad
def f_binomial(n, k, p):
    return n_combinatory(n, k) * math.pow(p, k) * math.pow((1 - p), (n - k))

## Funciones media, varianza y desviación típica
def mean(n, p):
    return n * p

def variance(n, p):
    return n * p * (1 - p)

def standard_error(n, p):
    return math.sqrt(n * p * (1 - p))