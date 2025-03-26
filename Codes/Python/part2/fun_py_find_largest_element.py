# fun_py_find_largest_element.py

def fun_py_find_largest_element(lst):
    return max(lst)

def test_find_largest_element():
    numbers = [10, 25, 34, 89, 67]
    print(f"Largest number: {fun_py_find_largest_element(numbers)}")

if __name__ == "__main__":
    test_find_largest_element()
