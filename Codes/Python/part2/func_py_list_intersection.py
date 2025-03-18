# func_py_list_intersection.py

def func_py_list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def test_list_intersection():
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]
    print(f"Intersection: {func_py_list_intersection(a, b)}")

if __name__ == "__main__":
    test_list_intersection()
