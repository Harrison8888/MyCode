# func_py_calculate_catenary_length.py
import math

def func_py_calculate_catenary_length(a, x1, x2):
    return a * (math.sinh(x2/a) - math.sinh(x1/a))

print(func_py_calculate_catenary_length(2, 1, 3))
