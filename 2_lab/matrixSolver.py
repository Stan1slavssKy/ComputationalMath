import numpy as np
from numpy.linalg import inv, eigvals

#======================================================================

def fillInMatrix():
    n = 9
    A = np.full((n + 1, n + 1), 0, dtype = np.float64) # create zeroes matrix

    A[0, 0] = 1 # fill in first row in matrix

    for i in range (1, n):
        for j in range (0, n):
            if (i == j):
                 A[i][j] = -2
                 A[i][j - 1] = 1
                 A[i][j + 1] = 1

    # fill in last row
    A[n, 0] = A[n, n] = 1
    for i in range(1, n):
        A[n][i] = 2

    return A

def fillInVectorF():
    n = 9
    f = np.zeros(n + 1, dtype = np.float64)
    f[0] = 1
    f[n] = (-n) / 3
    for i in range(1, n):
        f[i] = 2 / ((i + 1)**2)
    
    return f

#======================================================================

def vectorNorm3(vec):
    return float(np.sqrt(np.dot(vec.T, vec)))

#======================================================================

def matrixNorm1(matr):
    norm = 0.0
    rowNumber = matr.shape[0]
    colNumber = matr.shape[1]
    for i in range(0, rowNumber):
        lineSum = 0
        for j in range(0, colNumber):
            lineSum += np.abs(matr[i][j])
        if (lineSum > norm):
            norm = lineSum
    
    return norm

def matrixNorm2(matr):
    norm = 0.0
    rowNumber = matr.shape[0]
    colNumber = matr.shape[1]
    for j in range(0, colNumber):
        lineSum = 0
        for i in range(0, rowNumber):
            lineSum += np.abs(matr[i][j])
        if (lineSum > norm):
            norm = lineSum
    
    return norm

def matrixNorm3(matr):
    transpMatr = matr.transpose()
    eigenValues = eigvals(np.dot(transpMatr, matr))
    return np.sqrt(max(eigenValues))

def findOptimalNorm(matr):
    invMatr = inv(matr)
    mu1 = matrixNorm1(matr) * matrixNorm1(invMatr)
    mu2 = matrixNorm2(matr) * matrixNorm2(invMatr)
    mu3 = matrixNorm3(matr) * matrixNorm3(invMatr)
    print('Число обусловленности для 1 нормы матрицы: ', mu1)
    print('Число обусловленности для 2 нормы матрицы: ', mu2)
    print('Число обусловленности для 3 нормы матрицы: ', mu3)

#======================================================================

def findMaxEigenValue(matr):
    iterations = 500
    maxEigenValue = 0.0
    prevVector = np.full(matr.shape[0], 5, dtype = np.float64)
    currentVector = prevVector

    for i in range(0, iterations):
        prevVector = currentVector
        currentVector = np.matmul(matr, currentVector)

    maxEigenValue = np.max(np.abs(currentVector[5] / prevVector[5]))

    return maxEigenValue

def findMinEigenValue(matr):
    return 1 / findMaxEigenValue(inv(matr))

#======================================================================

def isLUApplicable(matr):
    result = True
    n = matr.shape[0]

    for i in range(0, n):
        if (np.linalg.det(matr[:i, :i]) == 0):  
            result = False
    
    return result

def LUDecomposition(matr):
    n = matr.shape[0]

    L = np.eye(n, dtype = 'float64')
    U = np.full((n, n), 0, dtype = 'float64')

    for i in range(n):
        for j in range(n):
            if i <= j:
                U[i, j] = matr[i, j]
                for k in range(i):
                    U[i, j] -= L[i, k] * U[k, j]
            else:
                L[i, j] = 1 / U[j, j] * matr[i, j]
                for k in range(j):
                    L[i, j] -= 1 / U[j, j] * L[i, k] * U[k, j]
        
    return L, U

def LUSolveEquation(matr, f):
    # LUx = f => Ly = f & Ux = y
    L, U = LUDecomposition(matr)
    n = matr.shape[0]

    # Ly = f
    y = np.zeros(n)
    for i in range(0, n):
        y[i] = f[i]
        for j in range(0, i):
            y[i] -= L[i, j] * y[j]
        y[i] /=  L[i, i]

    # Ux = f
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(n - 1, i, -1):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    print('Невязка LU разложения:', vectorNorm3(f - matr.dot(x)))

    return x

#======================================================================

def upperRelaxationMethod(matr, f):
    D = np.diag(np.diag(matr))
    L = np.tril(matr) - D
    U = np.triu(matr) - D
    n = matr.shape[0]
    omega = 1
    eps = 1e-6
    u = np.zeros(n)

    B   = (- inv(D + omega * L)).dot((omega - 1) * D + omega * U)
    F = omega * (inv(D + omega * L)).dot(f)

    k = 0

    while (vectorNorm3(f - matr.dot(u)) > eps):
        u = B.dot(u) + F
        k += 1

    print('Невязка метода верхней релаксации:', vectorNorm3(f - matr.dot(u)))
    print("Критерий останова: невязка < eps = 1e-6")

def main():
    A = fillInMatrix()
    f = fillInVectorF()
    findOptimalNorm(A)
    maxEigenValue = findMaxEigenValue(A)
    minEigenValue = findMinEigenValue(A)
    print('Cтепенной метод: lambda_max =', maxEigenValue)
    print('Cтепенной метод: lambda_min =', minEigenValue)
    print('Применимо ли LU разложени? -', isLUApplicable(A))

    LUSolveEquation(A, f)
    upperRelaxationMethod(A, f)

#======================================================================
  
if __name__ == '__main__':
    main()