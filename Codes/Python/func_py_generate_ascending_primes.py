# func_py_generate_ascending_primes.py
def func_py_generate_ascending_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

print(func_py_generate_ascending_primes(100))
