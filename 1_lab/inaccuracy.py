import matplotlib.pyplot as plt
import numpy as np
from sympy import *

INPUT_POINT = 10

#======================================================================================================================

x = symbols('x')
functions = [sin(x * x), cos(sin(x)), exp(sin(cos(x))), ln(x + 3), (x + 3) ** (1 / 2)]

#======================================================================================================================

def approxDerivative1(function, x, h):
    return (function(x + h) - function(x)) / h

def approxDerivative2(function, x, h):
    return (function(x) - function(x - h)) / h

def approxDerivative3(function, x, h):
    return (function(x + h) - function(x - h)) / (2 * h)

def approxDerivative4(function, x, h):
    frac1 = (function(x + h) - function(x - h)) / (2 * h)
    frac2 = (function(x + 2 *  h) - function(x - 2 * h)) / (4 * h)
    derivate = (4 / 3) * frac1 - (1 / 3) * frac2
    return derivate

def approxDerivative5(function, x, h):
    frac1 = (function(x + h) - function(x - h)) / (2 * h)
    frac2 = (function(x + 2 *  h) - function(x - 2 * h)) / (4 * h)
    frac3 = (function(x + 3 *  h) - function(x - 3 * h)) / (6 * h)
    derivate = (3 / 2) * frac1 - (3 / 5) * frac2 + (1 / 10) * frac3
    return derivate

approxDerivative = [approxDerivative1, approxDerivative2, approxDerivative3, approxDerivative4, approxDerivative5]

#======================================================================================================================

def absoluteErrorCalculation(function, method, point, h, derivative):
    return np.abs(method(function, point, h) - derivative(point))

def getDerivativeLambda(function):
    derivativeLambda = lambdify(x, diff(function))
    return derivativeLambda

def createPlot(errors, h, name):
    plt.plot(np.log(h), np.log(errors), '.-', markersize = 9, label = name)
    plt.grid(True)

def getErrors(function, method, derivative):
    errors = np.empty(21)
    h      = np.empty(21)
    for i in range(1, 22):
        h[i - 1] = 2 ** (1 - i)
        errors[i - 1] = absoluteErrorCalculation(function, method, INPUT_POINT, h[i - 1], derivative)
    return errors, h

def main():
    for func in functions:
        plt.figure(figsize=(8,8))
        plt.title(r"График ошибки вычисления производной для функции " + str(func))
        plt.ylabel(r"$ln(\Delta)$")
        plt.xlabel(r"$ln(h_n), h_n = 2 / 2^n, n = \overline{1, 21}$")

        x = symbols('x')
        derivative = getDerivativeLambda(func)

        for i in range(len(approxDerivative)):
            errors, h = getErrors(lambdify(x, func), approxDerivative[i], derivative)
            methodName = "method "+ str(i + 1)
            createPlot(errors, h, methodName)

        plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)
        plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')
        plt.minorticks_on()
        plt.tight_layout()
        plt.legend(loc='best', fontsize = 12)
        plt.savefig("images/f" + str(func) + ".png")

#======================================================================================================================

if __name__ == "__main__":
    main()