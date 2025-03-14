# func_py_hamming_distance.py

def func_py_hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def test_hamming_distance():
    pairs = [("karolin", "kathrin"), ("hello", "h3llo"), ("1011101", "1001001")]
    for s1, s2 in pairs:
        print(f"Hamming distance between '{s1}' and '{s2}': {func_py_hamming_distance(s1, s2)}")

if __name__ == "__main__":
    test_hamming_distance()
