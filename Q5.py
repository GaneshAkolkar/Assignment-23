def generate_fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Example usage:
n = 5
fib_gen = generate_fibonacci(n)
for term in fib_gen:
    print(term)
