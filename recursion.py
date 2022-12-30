"""Рекурсия на примере нахождения факториала"""


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
