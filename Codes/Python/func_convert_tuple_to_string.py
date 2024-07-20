# func_convert_tuple_to_string.py
def func_convert_tuple_to_string(tpl):
    return ''.join(map(str, tpl))

print(func_convert_tuple_to_string((1, 2, 3, 4, 5)))
