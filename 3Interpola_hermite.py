# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:05:34 2019

@author: josec
"""

from numpy.polynomial.hermite import hermfit,hermval
import numpy as np

x=np.array([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])
y=np.array([6115108363,6194460444,6273526441,6352677699,6432374971,6512602867,6593623202,6675130418,6757887172,6840591577,6922947261,7004011262,7086993625,7170961674,7255653881,7340548192,7426103221])
Polinomio=hermfit(x,y,16)#Retorna os coeficientes do Polinômio de Hermite.
print(Polinomio)




