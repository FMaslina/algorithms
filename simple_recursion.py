def countdown(i):
    if i <= 0:
        return None
    else:
        print(i)
        countdown(i - 1)


countdown(996)