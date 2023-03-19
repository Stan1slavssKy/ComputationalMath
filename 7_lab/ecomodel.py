import numpy as np
from matplotlib import pyplot as plt
import sympy as sp
from sympy import Matrix

#======================================================================================================
# Task conditions
eps  = 0.0001
x_0  = 0
y_0  = 1
a_10 = 0.05
a_20 = 10
T_k  = 2000

# Constants for Rosenbrok method
p_1  = 0.435866521508459
p_2  = 0.4782408332745185
p_3  = 0.0858926452170225
a    = p_1
b_21 = p_1
b_31 = p_1
b_32 = -2.116053335949811

#======================================================================================================

def print_jacobian():
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    a_1 = sp.Symbol('a_1')
    a_2 = sp.Symbol('a_2')
    system_matrix = Matrix([x * (2 * a_1 - 0.5 * x - y * (a_1 ** 2) * (a_2 ** (-2))), 
                           y * (2 * a_2 - 0.5 * y - x * (a_2 ** 2) * (a_1 ** (-2))), 
                           eps * (2 - 2 * y * a_1 * a_2 ** (-2)), 
                           eps * (2 - 2 * x * a_2 * a_1 ** (-2))])
    variables = Matrix([x, y, a_1, a_2])
    jacobian = system_matrix.jacobian(variables)
    print(jacobian)
    return jacobian


def jacobian(vec):
    x, y, a_1, a_2 = vec[0], vec[1], vec[2], vec[3]

    return np.array([[-a_1 ** 2 * y * a_2 ** (-2) + 2 * a_1 - x, -a_1 ** 2 * x * a_2 ** (-2), x * (-2 * a_1 * y * a_2 ** (-2) + 2), 2*a_1**2 * x * y * a_2 ** (-3)], 
                     [-a_2 ** 2 * y * a_1 ** (-2), -a_2 ** 2 * x * a_1 ** (-2) + 2 * a_2 - y, 2 * a_2 ** 2 * x * y * a_1 ** (-3), y*(-2*a_2*x * a_1**(-2) + 2)], 
                     [0, -0.02 * a_1 * a_2 ** (-2), -0.02 * y * a_2 ** (-2), 0.04 * a_1 * y * a_2 ** (-3)], 
                     [-0.02 * a_2 * a_1 ** (-2), 0, 0.04 * a_2 * x * a_1 ** (-3),   -0.02 * x  * a_1 ** (-2)]])

def func(vec):
    x, y, a_1, a_2 = vec[0], vec[1], vec[2], vec[3]

    return np.array([x * (2 * a_1 - 0.5 * x - y * (a_1 ** 2) * (a_2 ** (-2))), 
                    y * (2 * a_2 - 0.5 * y - x * (a_2 ** 2) * (a_1 ** (-2))),
                    eps * (2 - 2 * y * a_1 * a_2 ** (-2)),
                    eps * (2 - 2 * x * a_2 * a_1 ** (-2))])

def D_n(vec, h):
    return np.eye(4) + a * h * jacobian(vec)

def method_Rosenbrok_3_order(start_vector, h, num_steps):
    result = np.zeros((num_steps, np.shape(start_vector)[0]))
    result[0] = start_vector
    
    for i in range(0, num_steps - 1):
        Dn = D_n(result[i], h)
        
        dk_1 = h * func(result[i])
        k_1 = np.linalg.solve(Dn, dk_1)
        dk_2 = h * func(result[i] + b_21 * k_1)
        k_2 = np.linalg.solve(Dn, dk_2)
        dk_3 = h * func(result[i] + b_31 * k_1 + b_32 * k_2)
        k_3 = np.linalg.solve(Dn, dk_3)

        result[i + 1] = result[i] + p_1 * k_1 + p_2 * k_2 + p_3 * k_3
    return result

def draw_Rosenbrok_result(result, t):
    result = result.T
    plt.figure(figsize=[16, 8])

    labels = ["x(t)", "y(t)", "a1(t)", "a2(t)"]
    
    for i in range(len(result)):
        plt.plot(t, result[i], label=labels[i])

    plt.title('Решения для экогенетической модели')

    plt.xlabel("t")
    plt.ylabel("x")
    plt.minorticks_on()
    plt.tight_layout()
    plt.legend(loc = 'best', fontsize = 12)
    plt.savefig('images/solve.png')
    
    return

def main():
    # print_jacobian()
    h = 0.01
    num_steps = int(T_k / h) + 1
    t = np.linspace(0, T_k, num_steps)
    
    start_vector = np.array([x_0, y_0, a_10, a_20])
    result = method_Rosenbrok_3_order(start_vector, h, num_steps)
    draw_Rosenbrok_result(result, t)
    return

if __name__ == "__main__":
    main()
