# func_py_calculate_cycloid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_cycloid_curve(radius, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = radius * (t - np.sin(t))
    y = radius * (1 - np.cos(t))
    plt.plot(x, y)
