# func_py_find_largest_even_number.py
def func_py_find_largest_even_number(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return max(even_numbers) if even_numbers else None

print(func_py_find_largest_even_number([1, 3, 5, 8, 10, 2]))
