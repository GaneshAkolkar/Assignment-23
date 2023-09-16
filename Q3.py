def generate_even_numbers(n):
    num = 2
    count = 0
    while count < n:
        yield num
        num += 2
        count += 1

# Example usage:
n = 5
even_gen = generate_even_numbers(n)
for num in even_gen:
    print(num)
