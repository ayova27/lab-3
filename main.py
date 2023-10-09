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

def task_6():
    user_input = str(input("String: "))

    index = 0

    result = None

    while index < len(user_input):
        result = user_input[::-1]
        index += 1

    print(result)


# task_6()


def task_7():
    user_input = int(input("Numbers: "))
    user_input = str(user_input)

    index = 0
    dauletsuper = []

    while index < len(user_input):
        superdaulet = int(user_input[index])
        if superdaulet % 2 != 0:
            dauletsuper.append(superdaulet)
            index += 1
        else:
            index += 1
            continue

    print(sum(dauletsuper))


# task_7()

def task_8():
    import random

    def task_8():
        numbers = [int(x) for x in range(1, 101)]
        random_element = random.choice(numbers)

        while True:
            user_choice = int(input("Введите число: "))

            if user_choice < random_element:
                hint = random_element - user_choice
                if hint >= 25:
                    print("Слишком маленькое число.")
                else:
                    print("Не слишком маленькое число.")

            elif user_choice > random_element:
                hint = user_choice - random_element
                if hint >= 25:
                    print("Слишком большое число!")
                else:
                    print("Не слишком большое число!")

            else:
                print("Поздравляю! Вы угадали число!")
                break
    task_8()
task_8()
