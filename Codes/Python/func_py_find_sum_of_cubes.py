# func_py_find_sum_of_cubes.py
def func_py_find_sum_of_cubes(n):
    return sum(x ** 3 for x in range(1, n + 1))

print(func_py_find_sum_of_cubes(3))
