import numpy as np
from matplotlib import pyplot as plt

def func(x, vec):
    y = vec[0]
    z = vec[1]
    return np.array([z, x * np.sqrt(y)])

#==============================================================================

def method_RK_4_order(x, start_vector, h, num_steps):
    result = np.zeros((num_steps, np.shape(start_vector)[0]))
    result[0] = start_vector
    integral_summ = 0

    for i in range(0, num_steps - 1):
        k_1 = func(x[i], result[i])
        k_2 = func(x[i] + h / 2, result[i] + 0.5 * h * k_1)
        k_3 = func(x[i] + h / 2, result[i] + 0.5 * h * k_2)
        k_4 = func(x[i] + h, result[i] + h * k_3)
        result[i + 1] = result[i] + h * (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6

        if(i != 0):
            integral_summ += (result[i][0] + result[i - 1][0]) / 2 * h
          
    return integral_summ, result

def draw_result_of_MRK(result, x):
    plt.figure(figsize = (6, 6))
    y, z = result.T

    plt.plot(x, y)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid()

    safe_name = 'images/Shooting.png'
    plt.savefig(safe_name)
    
    return

#==============================================================================

def main():
    x_0 = 0
    y_0 = 0
    z_0 = 1.5
    x_beg = 0
    x_end = 1
    h = 0.001
    
    num_steps = int((x_end - x_beg) / h) + 1
    x = np.linspace(x_beg, x_end, num_steps)
 
    integral_sum = 0
    result = np.empty((0), float)
    epsilon = 1e-4
    
    while(True):
        start_vector = np.array([y_0, z_0])
        integral_sum, result = method_RK_4_order(x, start_vector, h, num_steps)
        z_0 += 10 * epsilon
        if(abs(integral_sum - 1.0) < epsilon):
            print(integral_sum)
            break
    
    print(z_0)
    draw_result_of_MRK(result, x)
    return

if __name__ == "__main__":
    main()
