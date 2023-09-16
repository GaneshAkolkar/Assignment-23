def endless_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = endless_fibonacci()
for _ in range(10):
    print(next(fib_gen))
