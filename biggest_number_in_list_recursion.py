def get_biggest_number(arr):
    if len(arr) >= 2:
        if arr[1] > arr[0]:
            return get_biggest_number(arr[1:])
        else:
            return arr[0]
    else:
        return arr[0]


my_arr = [1, 2, 3, 4, 5, 6, 7]
print(get_biggest_number(my_arr))
