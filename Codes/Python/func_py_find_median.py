# func_py_find_median.py
def func_py_find_median(lst):
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

print(func_py_find_median([1, 2, 3, 4, 5]))
