from math import *


def task_1():
    count = int(input("Number: "))

    dauletsuper = 0
    print(1)

    while count >= dauletsuper:
        dauletsuper += 2
        print(dauletsuper)


# task_1()

def task_2():
    user_input = int(input("Number: "))
    factorial_user_input = []
    dauletsuper = 1

    while user_input != 0:
        factorial_user_input.append(user_input)
        user_input -= 1
        if user_input == 0:
            break

    for i in range(1, len(factorial_user_input) + 1):
        dauletsuper *= i

    print(dauletsuper)
    
task_2()
