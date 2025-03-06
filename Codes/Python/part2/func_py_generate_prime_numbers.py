# func_py_generate_prime_numbers.py
def func_py_generate_prime_numbers(n):
    primes = []
    for num in range(2, n+1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

print(func_py_generate_prime_numbers(50))
