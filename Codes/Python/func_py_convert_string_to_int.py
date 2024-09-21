# func_py_convert_string_to_int.py
def func_py_convert_string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None

print(func_py_convert_string_to_int("123"))
