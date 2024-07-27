# func_py_convert_binary_to_int.py
def func_py_convert_binary_to_int(binary_string):
    try:
        return int(binary_string, 2)
    except ValueError:
        return None

print(func_py_convert_binary_to_int("1010"))
print(func_py_convert_binary_to_int("abcd"))
