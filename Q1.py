my_set = {1, 2, 3, 4, 5}
iter_set = iter(my_set)
while True:
    try:
        element = next(iter_set)
        print(element)
    except StopIteration:
        break
