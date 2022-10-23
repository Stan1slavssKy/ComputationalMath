import numpy as np


#=============================================================================

def iterationFunction(x):
    return np.pi - np.arcsin(x**2 / 20.0)

def simpleIterationMethod(startPoint, nmbIterations):
    result = startPoint
    for i in range(0, nmbIterations):
        temp = result
        result = iterationFunction(result)
        if (np.abs(result - temp) < 1e-16):
            return result

    return result

#=============================================================================

def F1(x, y):
    return (-np.sin(y) * (np.sin(x + 1) - y - 1.2) - 2 * (2 * x  + np.cos(y) - 2)) / (-np.sin(y) * np.cos(x + 1) + 2)

def F2(x, y):
    return (1 * (np.sin(x + 1) - y - 1.2) + np.cos(x + 1) * (2 * x + np.cos(y) - 2)) / (-np.sin(y) * np.cos(x + 1) + 2) 


def NewtonMethod(startX, startY, nmbIterations, epsilon):
    x = startX
    y = startY

    for i in range(0, nmbIterations):
        tempX = x
        tempY = y
        x = x + F1(x, y)
        y = y + F2(x, y)
        if((tempX - x < epsilon) and (tempY - y < epsilon)):
            print(i)
            return (x, y)

    return (x, y)

#=============================================================================

def main():
    result = simpleIterationMethod(np.pi, 500)
    print(result)
    result = NewtonMethod(np.pi / 2, -np.pi / 2, 500, 1e-3)
    print(result)
    return

#=============================================================================

if __name__ == "__main__":
    main()