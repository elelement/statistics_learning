# statistics_learning
Ejercicios, teoría e implementación de todo tipo de funciones estadísticas. Se contemplarán distintas distribuciones, teorema de Bayes y programación bayesiana (fuente [](http://www.vitutor.com/pro/3/b_1.html).

Requisitos:

1. Instalar matplotlib:
- pip install matplotlib
- apt-get install python-matplotlib

### Distribuciones

- [x] Probabilidad
- [x] Binomial
- [x] Normal
- [ ] Poisson
- [ ] Otras

## Distribución binomial o de Bernouilli
Un experimento sigue el modelo de la distribución binomial o de Bernoulli si:
1. En cada prueba del experimento sólo son posibles dos resultados: el suceso A (éxito) y su contrario (fracaso).
2. La probabilidad del suceso A es constante, es decir, que no varía de una prueba a otra. Se representa por p.
3. El resultado obtenido en cada prueba es independiente de los resultados obtenidos anteriormente.

La distribución binomial se suele representar por B(n, p):
* n es el número de pruebas de que consta el experimento.
* p es la probabilidad de éxito.

La probabilidad del suceso contrario es 1 − p, y la representamos por q.

##### Variable aleatoria binomial
La variable aleatoria binomial, X, expresa el número de éxitos obtenidos en cada prueba del experimento.

La variable binomial es una variable aleatoria discreta, sólo puede tomar los valores 0, 1, 2, 3, 4, ..., n suponiendo que se han realizado n pruebas.

## La distribución normal
![curva distribución normal](http://www.vitutor.co.uk/pro/5/images/1.gif)
* El campo de existencia es cualquier valor real, es decir, (-∞, +∞).
* Es simétrica respecto a la media µ.
* Tiene un máximo en la media µ.
* Crece hasta la media µ y decrece a partir de ella.
* En los puntos µ − σ y µ + σ presenta puntos de inflexión.
* El eje de abscisas es una asíntota de la curva.

El área del recinto determinado por la función y el eje de abscisas es igual a la unidad.

Al ser simétrica respecto al eje que pasa por x = µ, deja un área igual a 0.5 a la izquierda y otra igual a 0.5 a la derecha.

La probabilidad equivale al área encerrada bajo la curva.
```
p(μ - σ < X ≤ μ + σ) = 0.6826 = 68.26 %
p(μ - 2σ < X ≤ μ + 2σ) = 0.954 = 95.4 %
p(μ - 3σ < X ≤ μ + 3σ) = 0.997 = 99.7 % 
```

##### Variable aleatoria continua
Una variable aleatoria continua, X, sigue una distribución normal de media μ y desviación típica σ, y se designa por N(μ, σ), si se cumplen las siguientes condiciones:

1. La variable puede tomar cualquier valor: (-∞, +∞)
2. La función de densidad, es la expresión en términos de ecuación matemática de la curva de Gauss:

##### Distribución normal estándar
La distribución normal estándar, o tipificada o reducida, es aquella que tiene por media el valor cero, μ = 0, y por desviación típica la unidad, σ =1.

Su función de densidad es:

![función de densidad](http://www.vitutor.co.uk/pro/5/images/6.gif)

Y su gráfica:

![gráfica f_densidad](http://www.vitutor.co.uk/pro/5/images/9.gif)

###### Tipificación de la variable
Para poder utilizar la tabla tenemos que transformar la variable X que sigue una distribución N(μ, σ) en otra variable Z que siga una distribución N(0, 1).

![tipificar](http://www.vitutor.co.uk/pro/5/images/10.gif)

### TODO
* Intentar paralelizar todos los cálculos independientes.
