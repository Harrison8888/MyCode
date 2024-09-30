# func_py_find_unique_numbers.py
def func_py_find_unique_numbers(lst):
    unique_numbers = []
    for num in lst:
        if lst.count(num) == 1:
            unique_numbers.append(num)
    return unique_numbers
