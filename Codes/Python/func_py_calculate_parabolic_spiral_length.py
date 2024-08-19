# func_py_calculate_parabolic_spiral_length.py
import math

def func_py_calculate_parabolic_spiral_length(a, theta):
    return (a / 2) * (math.sqrt(1 + theta**2) + math.log(theta + math.sqrt(1 + theta**2)))

print(func_py_calculate_parabolic_spiral_length(1, 5))
