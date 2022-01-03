def count(list):
    if not list:
        return 0
    return 1 + count(list[1:])


list = [1, 2, 3, 4, 5, 6]
print(count(list))