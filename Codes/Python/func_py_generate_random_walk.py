# func_py_generate_random_walk.py
import random
import matplotlib.pyplot as plt

def func_py_generate_random_walk(steps):
    x, y = [0], [0]
    for _ in range(steps):
        angle = random.uniform(0, 2 * 3.14159)
        x.append(x[-1] + random.cos(angle))
        y.append(y[-1] + random.sin(angle))
    plt.plot(x, y)
    plt.show()

func_py_generate_random_walk(1000)
