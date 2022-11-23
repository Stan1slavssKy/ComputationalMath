import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib as mpl

# filling in the input data, x - years, y - population
x = np.array([1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
y = np.array([92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203211926, 226545805, 248709873, 281421906])

#========================================================================================================

def getPolinomCoefs(diffMatrix):
    size = diffMatrix.shape[0]
    coefs = np.zeros(size)

    for i in range(size):
        coefs[i] = diffMatrix[i][0]

    return coefs

def getAllDivideDifferencesForPolinom(x, y):
    diffMatrix = np.zeros(shape = (y.size, y.size))

    for i in range(y.size): diffMatrix[0][i] = y[i]

    for i in range(1, y.size):
        for j in range(y.size - i):
            diffMatrix[i][j] = (diffMatrix[i - 1][j + 1] - diffMatrix[i - 1][j]) / (x[j + i] - x[j])
    return diffMatrix

def polinom(coefs, point, x):
    result = 0

    for i in range(coefs.size):
        temp = coefs[i]
        for j in range(i):
            temp *= (point - x[j])
        result += temp

    return result

def drawNewtonsInterpolation(x, y):
    diffMatrix = getAllDivideDifferencesForPolinom(x, y)
    coefs = getPolinomCoefs(diffMatrix)
    
    mpl.rcParams['font.size'] = 9
    plt.figure(figsize = (5,5), facecolor = "white")

    plt.title("Численность населения США")
    plt.ylabel("$N$")
    plt.xlabel("$год$")

    x_lin = np.linspace(x[0], 2010, 1000)

    plt.plot(x_lin, polinom(coefs, x_lin, x), "black", label = "Интерполянт Ньютона")
    plt.plot(x, y, 'or', markersize = 5, label = "Узлы интерполяции")
    plt.plot(2010, polinom(coefs, 2010, x), 'o', color='blue', markersize = 5, label = "Экстраполированная точка")
    plt.xlim(1900, 2020)
    plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)
    plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

    plt.minorticks_on()
    plt.tight_layout()
    plt.legend(loc = "best", fontsize = 9)
    plt.savefig('images/Newton.png')

    return

#========================================================================================================

def main():
    drawNewtonsInterpolation(x, y)
    return

if __name__ == "__main__":
    main()