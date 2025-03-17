# func_py_most_frequent.py

from collections import Counter

def func_py_most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]

def test_most_frequent():
    numbers = [1, 3, 3, 2, 1, 3, 4, 5, 3, 2, 1]
    print(f"Most frequent number: {func_py_most_frequent(numbers)}")

if __name__ == "__main__":
    test_most_frequent()
