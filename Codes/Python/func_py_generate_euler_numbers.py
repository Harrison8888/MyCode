# func_py_generate_euler_numbers.py
def func_py_generate_euler_numbers(n):
    euler = [1] + [0] * n
    for i in range(1, n + 1):
        euler[i] = euler[i - 1] * (2 * (2 * i - 1)) // i
    return euler

print(func_py_generate_euler_numbers(5))
