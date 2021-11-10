# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:21:13 2019

@author: josec
"""

from scipy.interpolate import lagrange
import numpy as np

x=np.array([-2,0,1,2])
y=np.array([-162,0,21,242])
Inter_lagran= lagrange(x,y)
print(Inter_lagran)

#calcular para os pontos requeridos na letra d uma vez que sabemos o polinômio de Lagrange

f_1=30*(-1)**3+10*(-1)**2-19*(-1)
f_3=30*3**3+10*3**2-19*3
print(f_1)
print(f_3)