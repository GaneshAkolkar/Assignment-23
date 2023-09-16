def generate_odd_numbers(n):
    num = 1
    count = 0
    while count < n:
        yield num
        num += 2
        count += 1

# Example usage:
n = 5
odd_gen = generate_odd_numbers(n)
for num in odd_gen:
    print(num)
