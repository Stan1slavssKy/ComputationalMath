import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#========================================================================================================
# Input data, x - years, y - population
x = np.array([1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
y = np.array([92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203211926, 226545805, 248709873, 281421906])

#========================================================================================================
# Newton interpolation

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
# Spline interpolation

def triangleRun(a, b, c, f):
    n = f.size
    p = np.zeros(n)
    r = np.zeros(n)
    x = np.zeros(n)

    # direct
    p[0] = c[0] / b[0]
    r[0] = f[0] / b[0]

    for k in range(1, n - 1):
        p[k] = c[k] / (b[k] - a[k] * p[k - 1])
        r[k] = (f[k] - a[k] * r[k - 1]) / (b[k] - a[k] * p[k - 1])

    # reverse
    x[n - 1] = r[n - 1]

    for k in range(n - 2, -1, -1):
        x[k] = r[k] - p[k] * x[k + 1]

    return x

def getSplineCoefsForTriangleRun(h, y):
    n = x.size
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    f = np.zeros(n)

    a[0] = 0
    b[0] = 1
    c[0] = 0
    f[0] = 0

    for k in range(1, n - 1):
        a[k] = h[k] / 6
        b[k] = (h[k] + h[k + 1]) / 3
        c[k] = h[k + 1] / 6
        f[k] = (y[k + 1] - y[k]) / h[k + 1] - (y[k] - y[k - 1]) / h[k]

    a[n - 1] = 0
    b[n - 1] = 1
    c[n - 1] = 0
    f[n - 1] = 0

    return a, b, c, f

def spline(a, b, c, d, x0):
    k = 0
    n = a.size
    if x0 <= x[1]:
        k = 1
    elif x0 > x[n - 1]:
        k = n - 1
    else:
        for i in range(1, n):
            if x0 > x[i - 1] and x0 <= x[i]:
                k = i
                break

    return a[k] + b[k] * (x0 - x[k]) + 1 / 2 * c[k] * ((x0 - x[k]) ** 2) + 1 / 6 * d[k] * ((x0 - x[k]) ** 3)

def getSpline(x, y):
    n = x.size
    h = np.zeros(n)
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    d = np.zeros(n)

    for k in range(1, h.size):
        h[k] = x[k] - x[k - 1]
    
    aT, bT, cT, fT = getSplineCoefsForTriangleRun(h, y)
    c = triangleRun(aT, bT, cT, fT)

    for k in range(1, n):
        a[k] = y[k]
        d[k] = (c[k] - c[k - 1]) / h[k]
        b[k] = 1 / 6 * (2 * c[k] + c[k - 1]) * h[k] + (y[k] - y[k - 1]) / h[k]

    def resultSpline(x0):
        return spline(a, b, c, d, x0)

    return resultSpline

def drawSpineInterpolation(x, y):
    spline = getSpline(x, y)
    
    mpl.rcParams['font.size'] = 9
    plt.figure(figsize = (5,5), facecolor = "white")

    plt.title("Численность населения США")
    plt.ylabel("$N$")
    plt.xlabel("$год$")

    x_lin = np.linspace(x[0], 2010, 1000)
        
    plt.plot(x_lin, [spline(x_lin[i]) for i in range(x_lin.size)], "black", label = "Аппроксимация сплайном")
    plt.plot(x, y, 'or', markersize = 5, label = "Узлы интерполяции")
    plt.plot(2010, spline(2010), 'o', color='blue', markersize = 5, label = "Экстраполированная точка")
    plt.xlim(1900, 2020)
    plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)
    plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

    plt.minorticks_on()
    plt.tight_layout()
    plt.legend(loc = "best", fontsize = 9)
    plt.savefig('images/Spline.png')

    return

#========================================================================================================

def main():
    diffMatrix = getAllDivideDifferencesForPolinom(x, y)
    coefs = getPolinomCoefs(diffMatrix)
    practicNewton = polinom(coefs, 2010, x)
    theoreticValue = 308745538

    spline = getSpline(x, y)
    practicSpline = spline(2010)

    print(coefs)

    print('[==========================Численность населения США в 2010 году==========================]')
    print('\t\tИнтерполяция методом Ньютона: ', practicNewton)
    print('\t\tИнтерполяция сплайнами: ', practicSpline)
    print('\t\tИстинное значние: ', theoreticValue)
    print('[=========================================================================================]')

    drawNewtonsInterpolation(x, y)
    drawSpineInterpolation(x, y)

    return

#========================================================================================================

if __name__ == "__main__":
    main()