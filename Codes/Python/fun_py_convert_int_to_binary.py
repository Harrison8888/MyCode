# fun_py_convert_int_to_binary.py
def fun_py_convert_int_to_binary(n):
    try:
        return bin(n)
    except TypeError:
        return None

print(fun_py_convert_int_to_binary(10))
print(fun_py_convert_int_to_binary(255))
