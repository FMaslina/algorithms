"""Решение, которое смог придумать я, не совсем верное, т.к.
   После этого из списка удаляются все элементы, и его больше нельзя использовать"""


def sum(arr):
    total = 0
    if not arr:
        return total
    else:
        total = arr.pop()
        return total + sum(arr)


def sum2(arr):      # Решение из книги
    if not arr:
        return 0
    return arr[0] + sum2(arr[1:])


my_arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum2(my_arr))
print(sum(my_arr))