# func_py_calculate_hexagonal_prism_volume.py
import math

def func_py_calculate_hexagonal_prism_volume(side_length, height):
    base_area = (3 * math.sqrt(3) / 2) * side_length**2
    return base_area * height

print(func_py_calculate_hexagonal_prism_volume(5, 10))
