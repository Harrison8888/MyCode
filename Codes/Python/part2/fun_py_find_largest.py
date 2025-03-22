# fun_py_find_largest.py

def fun_py_find_largest(lst):
    return max(lst)

def test_find_largest():
    numbers = [10, 25, 34, 89, 67]
    print(f"Largest number: {fun_py_find_largest(numbers)}")

if __name__ == "__main__":
    test_find_largest()
