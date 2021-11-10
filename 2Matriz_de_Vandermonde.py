# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:58:59 2019

@author: josec
"""

import numpy as np

x=np.array([-2,0,1,2])
N=4
y=np.vander(x,N, increasing=True)
print(y)