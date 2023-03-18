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

def draw_result_of_MRK(result, t):
    plt.figure(figsize = (6, 6))
    x, z = result.T

    ax = plt.axes(projection = '3d')
    
    # Data for a three-dimensional line
    ax.plot3D(x, z, t, 'gray')
    # Data for three-dimensional scattered points
    t_data = np.linspace(0, 100, 100);
    ax.scatter3D(x, z, t, c = t, cmap='Greens');
    
    ax.set_title('Result for e = 80');

    plt.savefig('images/solve_80.png')
    
    return

def main():
    e = 80
    start_vector = np.array([2, 0])
    h = 0.01
    t_beg = 0 # 0 < t <= 100
    t_end = 100
    num_steps = int((t_end - t_beg) / h) + 1
    t = np.linspace(t_beg, t_end, num_steps)
    result = method_RK_4_order(e, start_vector, h, num_steps, t)
    draw_result_of_MRK(result, t)

    return

if __name__ == "__main__":
    main()
