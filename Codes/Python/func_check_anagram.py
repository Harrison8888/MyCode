# func_check_anagram.py
def func_check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(func_check_anagram("listen", "silent"))
