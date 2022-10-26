import numpy as np

#=============================================================================

def iterationFunction(x):
    return np.pi - np.arcsin(x**2 / 20.0)

def simpleIterationMethod(startPoint, nmbIterations, epsilon):
    result = startPoint
    for i in range(0, nmbIterations):
        temp = result
        result = iterationFunction(result)
        if (np.abs(result - temp) < epsilon):
            return result, i

    return result

#=============================================================================

def F(vec):
    F = np.array([[0.0], [0.0]])
    F[0] = np.sin(vec[0] + 1.0) - vec[1] - 1.2
    F[1] = 2 * vec[0] + np.cos(vec[1]) - 2.0
    return F

def Jacobian(vec):
    J = np.identity(2)
    J[0, 0] = np.cos(vec[0] + 1.0)
    J[0, 1] = -1.0
    J[1, 0] = 2.0
    J[1, 1] = -np.sin(vec[1])
    return J

def normVec3(vec):
    return float(np.sqrt(np.dot(vec.transpose(), vec)))

def NewtonMethod(startPoint, F, J, epsilon, nmbIterations):
    result = startPoint

    for i in range(0, nmbIterations):
        temp   = result
        result = result - np.matmul(np.linalg.inv(Jacobian(result)), F(result))
        if(normVec3(result - temp) < epsilon):
            return result, i

    return result

#=============================================================================

def main():
    result, i = simpleIterationMethod(np.pi, 500, 1e-16)
    print(result, ' ', i)
    result, i = NewtonMethod(np.array([[0.3], [-0.5]]), F, Jacobian, 1e-3, 500)
    print(result, ' ', i)
    return

#=============================================================================

if __name__ == "__main__":
    main()