def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    num = 2
    count = 0
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Example usage:
n = 5
prime_gen = generate_primes(n)
for prime in prime_gen:
    print(prime)
