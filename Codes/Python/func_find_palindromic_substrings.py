# func_find_palindromic_substrings.py
def func_find_palindromic_substrings(string):
    length = len(string)
    palindromes = []
    for i in range(length):
        for j in range(i, length):
            substr = string[i:j+1]
            if substr == substr[::-1]:
                palindromes.append(substr)
    return palindromes

print(func_find_palindromic_substrings("abacdfgdcaba"))
