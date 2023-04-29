import numpy as np
import matplotlib.pyplot as plt

#===================================================================
# point of discontinuity
x0 = 1 / np.sqrt(2)

#===================================================================

def k(x):
    if (x < x0):
        return np.exp(np.sin(x))
    elif (x > x0):
        return 1

def q(x):
    if (x < x0):
        return 2
    if (x > x0):
        return 1

def f(x):
    if (x < x0):
        return np.exp(x)
    if (x > x0):
        return np.exp(x)

#===================================================================

def SolveBoundaryValueProblem(h):
    x_start = 0
    x_end = 1
    u_0 = 0 # u(0) = 0
    u_L = 1 # u(1) = 1

    L = int(1 / h) + 1
    x = np.linspace(x_start, x_end, L)
    
    u = np.zeros(L)
    u[0] = u_0
    u[-1] = u_L

    l_alpha = int(np.floor(x0 / h))
    l_beta = l_alpha + 1

    a = np.zeros(L)
    b = np.zeros(L)
    c = np.zeros(L)
    d = np.zeros(L)

    alpha = np.zeros(L)
    beta  = np.zeros(L)
    
    # direct run-through method begins
    for l in range(1, l_alpha):
        a[l] = k((l + 0.5) * h)
        b[l] = -(k((l + 0.5) * h) + k((l - 0.5) * h) + q(l * h) * h * h)
        c[l] = k((l - 0.5) * h)
        d[l] = -f(l * h) * h * h

    for l in range(l_beta + 1, L - 1):
        a[l] = k((l + 0.5) * h)
        b[l] = -(k((l + 0.5) * h) + k((l - 0.5) * h) + q(l * h) * h * h)
        c[l] = k((l - 0.5) * h)
        d[l] = -f(l * h) * h * h
    
    alpha[1] = -a[1] / b[1]
    beta[1]  = (d[1] - c[1] * u_0) / b[1]

    alpha[L - 2] = -c[L - 2] / b[L - 2]
    beta[L - 2]  = (d[L - 2] - c[L - 2] * u_L) / b[L - 2]   
    
    for l in range(2, l_alpha):
        alpha[l] = -a[l] / (b[l] + c[l] * alpha[l - 1])
        beta[l]  = (d[l] - c[l] * beta[l - 1]) / (b[l] + c[l] * alpha[l - 1])

    for l in range(L - 3, l_beta, -1):
        alpha[l] = -c[l] / (b[l] + a[l] * alpha[l + 1])
        beta[l]  = (d[l] - a[l] * beta[l + 1]) / (b[l] + a[l] * alpha[l + 1])
    
    u[l_alpha] = (k(l_alpha * h) * beta[l_alpha - 1] + k(l_beta * h) * beta[l_beta + 1]) / (k(l_alpha * h) * (1 - alpha[l_alpha - 1]) + k(l_beta * h) * (1 - alpha[l_beta + 1]))
    u[l_beta] = u[l_alpha].copy()

    u[l_alpha - 1] = alpha[l_alpha - 1] * u[l_alpha] + beta[l_alpha - 1]
    u[l_beta + 1] = alpha[l_beta + 1] * u[l_beta] + beta[l_beta + 1]

    # reverse run-through method begins
    for l in range(l_alpha - 1, 0, -1):
        u[l] = alpha[l] * u[l + 1] + beta[l]

    for l in range(l_beta + 1, L - 1):
        u[l] = alpha[l] * u[l - 1] + beta[l]
 
    return x, u

#===================================================================

def DrawResult(x, u):
    plt.plot(x, u)
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.grid()
    plt.title("Решение краевой задачи")
    
    plt.vlines(x0, min(u), max(u), colors="red", linestyles="dashed", label="Граница разрыва")
    plt.legend(loc = 'best', fontsize = 'small')
    plt.savefig("images/boundary_value_problem.png")
    
    return

#===================================================================

def main():
    h = 0.0001
    x, u = SolveBoundaryValueProblem(h)
    DrawResult(x, u)
    return

if __name__ == "__main__":
    main()
