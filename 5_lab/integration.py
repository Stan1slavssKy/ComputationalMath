import numpy as np
from matplotlib import pyplot as plt

# The function is given tabularly
x = np.array([0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0])
y = np.array([0.0, 0.021470, 0.293050, 0.494105, 0.541341, 0.516855, 0.468617, 0.416531, 0.367879])

def TrapezoidMethod(y,  h):
    result = y[0] + y[-1]
    for i in range(1, y.size - 1):
        result += 2 * y[i]

    return result * h / 2

def RichardsonsExtrapolation(y, h):
    result = y[0] + y[-1]
    for i in range(2, y.size - 1):
        if i % 2 == 0:
            result += 2 * y[i]

    return result * h

def SimpsonsMethod(y, h):
    result = y[0] + y[-1]
    for i in range(1, y.size - 1):
        if i % 2 == 0:
            result += 2 * y[i]
        else:
            result += 4 * y[i]

    return result * h / 3

def main():
    h = x[1] - x[0]
    print('Сalculation of a certain integral by the trapezoid method: I =', TrapezoidMethod(y, h))
    print('Сalculation of a certain integral by the trapezoid method with refinement of the result by Richardson extrapolation: I =', RichardsonsExtrapolation(y, h))
    print('Сalculation of a certain integral by Simpsons method: I =', SimpsonsMethod(y, h))
    return

if __name__ == "__main__":
    main()
