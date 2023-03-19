import numpy as np
from matplotlib import pyplot as plt

def func(e, vec):
    x = vec[0]
    z = vec[1]
    return np.array([z, e * (1 - x**2) * z - x])

def method_RK_4_order(e, start_vector, h, num_steps, t_end):
    result = np.zeros((num_steps, np.shape(start_vector)[0]))
    result[0] = start_vector

    for i in range(0, num_steps - 1):
        k_1 = func(e, result[i])
        k_2 = func(e, result[i] + 0.5 * h * k_1)
        k_3 = func(e, result[i] + 0.5 * h * k_2)
        k_4 = func(e, result[i] + h * k_3)
        result[i + 1] = result[i] + h * (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    return result

def draw_result_of_MRK(result, t, e, h):
    plt.figure(figsize = (6, 6))
    x, z = result.T

    ax = plt.axes(projection = '3d')
    
    # Data for a three-dimensional line
    ax.plot3D(x, z, t, 'green')
    
    ax.set_title('Result for e = %.2f, h = %.4f' % (e, h))
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    ax.set_zlabel('t')
    
    safe_name = 'images/MRK_solve_' + str(e) + '.png'
    plt.savefig(safe_name)
    
    return

def solve_with_MRK():
    t_beg = 0 # 0 < t <= 100
    t_end = 100
    
    e = 0.02
    h = 0.01
    start_vector = np.array([2, 0]) # x(0) = 2, z(0) = 0
    num_steps = int((t_end - t_beg) / h) + 1
    t = np.linspace(t_beg, t_end, num_steps)
    result = method_RK_4_order(e, start_vector, h, num_steps, t)
    draw_result_of_MRK(result, t, e, h)
    
    e = 10
    h = 0.01
    start_vector = np.array([2, 0]) # x(0) = 2, z(0) = 0
    num_steps = int((t_end - t_beg) / h) + 1
    t = np.linspace(t_beg, t_end, num_steps)
    result = method_RK_4_order(e, start_vector, h, num_steps, t)
    draw_result_of_MRK(result, t, e, h)
    
    e = 50
    h = 0.001
    start_vector = np.array([2, 0]) # x(0) = 2, z(0) = 0
    num_steps = int((t_end - t_beg) / h) + 1
    t = np.linspace(t_beg, t_end, num_steps)
    result = method_RK_4_order(e, start_vector, h, num_steps, t)
    draw_result_of_MRK(result, t, e, h)
    
    e = 90
    h = 0.0001
    start_vector = np.array([2, 0]) # x(0) = 2, z(0) = 0
    num_steps = int((t_end - t_beg) / h) + 1
    t = np.linspace(t_beg, t_end, num_steps)
    result = method_RK_4_order(e, start_vector, h, num_steps, t)
    draw_result_of_MRK(result, t, e, h)
    
    return

def main():
    solve_with_MRK()
    return

if __name__ == "__main__":
    main()
