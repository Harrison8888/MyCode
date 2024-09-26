# func_py_find_vowel_count.py
def func_py_find_vowel_count(s):
    return sum(1 for char in s.lower() if char in "aeiou")

print(func_py_find_vowel_count("hello world"))
