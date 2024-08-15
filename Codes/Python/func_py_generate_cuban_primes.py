# func_py_generate_cuban_primes.py
def func_py_generate_cuban_primes(limit):
    cuban_primes = []
    for i in range(1, limit + 1):
        candidate = 3 * i**2 + 3 * i + 1
        if all(candidate % j != 0 for j in range(2, int(candidate**0.5) + 1)):
            cuban_primes.append(candidate)
    return cuban_primes

print(func_py_generate_cuban_primes(100))
