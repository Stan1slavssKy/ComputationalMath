import matplotlib.pyplot as plt
import numpy as np
from sympy import *

INPUT_POINT = 10

#=============================================================================

def sinXsquare(x):
    return np.sin(x ** 2)

def sinXsquareDiff(x):
    return 2 * x * np.cos(x ** 2)

#=============================================================================

def absoluteErrorCalculation(function, method, point, h, derivative):
    print(method(function, point, h))
    print(derivative(point))
    print(h)
    return np.abs(method(function, point, h) - derivative(point))

def firstMethod(function, point, h):
    return (function(point + h) - function(point)) / (h)

#=============================================================================

errors = np.array([absoluteErrorCalculation(sinXsquare, firstMethod, INPUT_POINT, 2 ** (1 - i), sinXsquareDiff) for i in range(1, 22)])
h = np.array([2 ** (1 - i) for i in range(1, 22)])

plt.figure(figsize=(12, 7))
plt.plot(np.log(h), np.log(errors), 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
plt.grid(True)
plt.show()