# fun_py_generate_fibonacci_recursive.py

def fun_py_generate_fibonacci_recursive(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fun_py_generate_fibonacci_recursive(n - 1, memo) + fun_py_generate_fibonacci_recursive(n - 2, memo)
    return memo[n]

def test_generate_fibonacci_recursive():
    print(f"10th Fibonacci: {fun_py_generate_fibonacci_recursive(10)}")

if __name__ == "__main__":
    test_generate_fibonacci_recursive()
