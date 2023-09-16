def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

# Example usage:
n = 5
squares_gen = generate_squares(n)
for square in squares_gen:
    print(square)
