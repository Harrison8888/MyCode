# func_py_calculate_cone_volume.py
import math

def func_py_calculate_cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

print(func_py_calculate_cone_volume(3, 5))
