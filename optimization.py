from math import *

user_input = int(input("Number: "))


def optimization(n):
    if n == 0:
        return 1

    f = 1
    number = 0

    while user_input > number:
        number += 1
        f = f * number

    return f


print(optimization(user_input))
