# fun_py_generate_permutations.py
from itertools import permutations

def fun_py_generate_permutations(lst):
    return list(permutations(lst))

print(fun_py_generate_permutations([1, 2, 3]))
