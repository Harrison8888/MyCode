# func_py_sum_of_multiples.py
def func_py_sum_of_multiples(n, limit):
    return sum(i for i in range(1, limit+1) if i % n == 0)

print(func_py_sum_of_multiples(3, 10))
