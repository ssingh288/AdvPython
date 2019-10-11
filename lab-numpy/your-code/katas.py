# -*- coding: utf-8 -*-

################### WEIRD MATRIX MULTIPLICATIONS
import numpy as np

A = [[2]]

B = [[1, 2], [3, 4]]

C = [[2, 3]]

D = [[40], [50]]

E = [[0, 1], [2, 3]]

F = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

G = [[1, 2], [3, 4]]

H = [[10, 20, 30], [40, 50, 60]]

g = np.array(E)
h = np.array(F)
GH = np.array(g*h)
print(GH)

arraylist = [[A, B], [C , D],[E, F] ,[G , H]]
    
##################### INSERT DASHES
