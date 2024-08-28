# func_py_calculate_bicorn_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_bicorn_curve(a, points):
    t = np.linspace(-2 * np.pi, 2 * np.pi, points)
    x = a * np.sin(t)
    y = a * np.sin(t) * np.cos(t)**2 / (1 + np.sin(t)**2)
    plt.plot(x, y)
    plt.title("Bicorn Curve")
    plt.show()

func_py_calculate_bicorn_curve(5, 1000)
