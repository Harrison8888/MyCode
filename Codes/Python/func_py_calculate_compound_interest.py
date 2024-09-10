# func_py_calculate_compound_interest.py
def func_py_calculate_compound_interest(p, r, t):
    return p * ((1 + r / 100) ** t)

print(func_py_calculate_compound_interest(1000, 5, 2))
