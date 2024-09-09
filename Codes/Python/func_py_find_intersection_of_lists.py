# func_py_find_intersection_of_lists.py
def func_py_find_intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(func_py_find_intersection_of_lists([1, 2, 3], [2, 3, 4]))
