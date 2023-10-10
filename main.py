from math import *
import random


def task_1():
    count = int(input("Number: "))

    dauletsuper = 0

    print(1)

    while count > dauletsuper:
        dauletsuper += 2
        print(dauletsuper)


# task_1()


def task_2():
    user_input = int(input("Number: "))

    def factorial(n):
        if n == 1:
            return 1

        f = 1
        i = 0

        while n > i:
            i += 1
            f = f * i

        return f

    print(factorial(user_input))


# task_2()

def task_3():
    user_input = int(input("Number: "))
    numbers = [int(x) for x in range(1, 1000)]

    while True:
        if user_input in numbers:
            print("We foung your number!", user_input)
            break
        else:
            print("Sorry loser!")
            break


# task_3()

def task_4():
    user_input = str(input("String: "))

    strings = []

    for i in user_input:
        strings += i

    counts = 0

    while len(strings):
        if 'a' in strings:
            strings.remove('a')
            counts += 1

    print(counts)


# task_4()

def task_5():
    user_input = int(input("Number: "))
    user_input = str(user_input)

    numbers = []

    index, result = 0, 0

    while index < len(user_input):
        numbers.append(int(user_input[index]))
        result += numbers[index]
        index += 1

    print(result)


# task_5()


def fibonnaci():
    f1, f2 = 0, 1
    user_input = int(input("Number: "))
    dauletsuper = []

    while user_input > f2:
        f1, f2 = f2, f1 + f2
        print(f2)


# fibonnaci()

# def task_7():
#     user_input = str(input("String: "))
#
#     index = 0
#
#     result = None
#
#     while index < len(user_input):
#         result = user_input[::-1]
#         index += 1
#
#     print(result)
#
#
# # task_7()
#
#
# def task_8():
#     user_input = int(input("Numbers: "))
#     user_input = str(user_input)
#
#     index = 0
#     dauletsuper = []
#
#     while index < len(user_input):
#         superdaulet = int(user_input[index])
#         if superdaulet % 2 != 0:
#             dauletsuper.append(superdaulet)
#             index += 1
#         else:
#             index += 1
#             continue
#
#     print(sum(dauletsuper))
#
#
# # task_8()
#
# def task_9():
#     import random
#
#     numbers = [int(x) for x in range(1, 101)]
#     random_element = random.choice(numbers)
#
#     while True:
#         user_choice = int(input("Введите число: "))
#
#         if user_choice < random_element:
#             hint = random_element - user_choice
#             if hint >= 25:
#                 print("Слишком маленькое число.")
#             else:
#                 print("Не слишком маленькое число.")
#
#         elif user_choice > random_element:
#             hint = user_choice - random_element
#             if hint >= 25:
#                 print("Слишком большое число!")
#             else:
#                 print("Не слишком большое число!")
#
#         else:
#             print("Поздравляю! Вы угадали число!")
#             break
#
# task_9()


def task_10():
    user_input = str(input("String: "))

    while True:
        dauletsuper = user_input[::-1]

        if dauletsuper == user_input:
            print("Yeah, sonofabitch!")
            break
        else:
            print("daulet super!")
            break


task_10()


def task_11():
    user_input_x = int(input("X: "))
    user_input_y = int(input("Y: "))

    n = 0

    while True:
        if user_input_y == 0:
            print("1")
            break

        if user_input_y >