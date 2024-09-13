# func_py_calculate_fibonacci.py
def func_py_calculate_fibonacci(n):
    if n <= 1:
        return n
    return func_py_calculate_fibonacci(n-1) + func_py_calculate_fibonacci(n-2)

print(func_py_calculate_fibonacci(10))
