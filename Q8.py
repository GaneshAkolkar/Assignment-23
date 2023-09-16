def endless_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Example usage:
prime_gen = endless_primes()
for _ in range(10):
    print(next(prime_gen))
