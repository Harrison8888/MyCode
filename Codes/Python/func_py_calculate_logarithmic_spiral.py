# func_py_calculate_logarithmic_spiral.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_logarithmic_spiral(a, b, points):
    t = np.linspace(0, 4 * np.pi, points)
    r = a * np.exp(b * t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    plt.plot(x, y)
    plt.title("Logarithmic Spiral")
    plt.show()

func_py_calculate_logarithmic_spiral(1, 0.1, 1000)
