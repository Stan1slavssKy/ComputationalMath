import numpy as np

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

def vectorNorm1(vec):
    norm = 0.0
    for i in range(0, vec.shape[0]):
        if (np.abs(vec[i]) > norm):
            norm = np.abs(vec[i])
    return norm

def main():
    A = fillInMatrix()
    f = fillInVectorF()

if __name__ == '__main__':
    main()