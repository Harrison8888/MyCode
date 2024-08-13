# func_py_calculate_pyramid_surface_area.py
import math

def func_py_calculate_pyramid_surface_area(base_length, height):
    slant_height = math.sqrt((base_length / 2)**2 + height**2)
    base_area = base_length**2
    lateral_area = 2 * base_length * slant_height
    return base_area + lateral_area

print(func_py_calculate_pyramid_surface_area(6, 7))
