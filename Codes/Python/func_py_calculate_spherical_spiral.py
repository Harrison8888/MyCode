# func_py_calculate_spherical_spiral.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_spherical_spiral(a, points):
    t = np.linspace(0, 4 * np.pi, points)
    x = a * np.sin(t) * np.cos(t)
    y = a * np.sin(t) * np.sin(t)
    z = a * np.cos(t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.title("Spherical Spiral")
    plt.show()

func_py_calculate_spherical_spiral(5, 1000)
