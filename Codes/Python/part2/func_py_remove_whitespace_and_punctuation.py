# func_py_remove_whitespace_and_punctuation.py
import string

def func_py_remove_whitespace_and_punctuation(s):
    return ''.join([char for char in s if char not in string.whitespace and char not in string.punctuation])
