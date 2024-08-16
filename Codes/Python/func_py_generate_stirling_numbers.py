# func_py_generate_stirling_numbers.py
def func_py_generate_stirling_numbers(n, k):
    if n == k == 0:
        return 1
    elif n == 0 or k == 0:
        return 0
    return k * func_py_generate_stirling_numbers(n - 1, k) + func_py_generate_stirling_numbers(n - 1, k - 1)

print(func_py_generate_stirling_numbers(5, 3))
