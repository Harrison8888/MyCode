# func_py_find_least_frequent_element.py
from collections import Counter

def func_py_find_least_frequent_element(lst):
    return Counter(lst).most_common()[-1][0]

print(func_py_find_least_frequent_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
