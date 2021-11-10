# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:08:39 2019

@author: josec
"""

#O Código original pertence a Dhiego Loyola só alterei os valores para os valores x e y em questão requeridos na questão número 3
import numpy
from matplotlib import pyplot

x = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
y = [6115108363,6194460444,6273526441,6352677699,6432374971,6512602867,6593623202,6675130418,6757887172,6840591577,6922947261,7004011262,7086993625,7170961674,7255653881,7340548192,7426103221,7510990456,7594270356]

n = len(x)


# determinar o coeficiente de Lagrange
def L(num, xi, x):
    prod = 1
    for xj in x:
        if xi != xj:
            prod *= (num-xj)/(xi-xj)
    return prod


# interpolar no ponto x = 3
zeta = 2017
L_n = [L(zeta, xi, x) for xi in x]


Lagrange = sum(yi*j for yi, j in zip(y, L_n))

# função para determinar o valor do polinômio de Lagrange
def P(z, x, y):
    return sum(yi*L(z, xi, x) for xi, yi in zip(x, y))

teste = P(2017, x, y)
f_2019= P(2019,x,y)
print(f_2019)

t = numpy.linspace(2000.1, 2019.1, num=50)
y_p = P(t, x, y)

fig = pyplot.figure(1)

pyplot.plot(t, 1/t, 'ro')
pyplot.plot(t, y_p, 'b-')

pyplot.show()
