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

def task_7():
    user_input = str(input("String: "))

    index = 0

    result = None

    while index < len(user_input):
        result = user_input[::-1]
        index += 1

    print(result)


# task_7()


def task_8():
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


# task_8()

def task_9():
    import random

    numbers = [int(x) for x in range(1, 101)]
    random_element = random.choice(numbers)

    while True:
        user_choice = int(input("Number: "))

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


# task_10()


def task_11():
    user_input_x = int(input("X: "))
    user_input_y = int(input("Y: "))

    n = 0

    if user_input_y == 0:
        print("1")
        return None

    while n < user_input_y:
        n += 1
        result = user_input_x ** n
        print(f'Power: {n} - {result}')


# task_11()

def task_12():
    def simple_number(n):
        for i in range(2, n + 1):
            if n == i:
                return True
            elif n % i == 0:
                return False
        return True

    result = []
    i = 3

    dauletsuper = int(input("Nubmer: "))

    while i < dauletsuper:
        i += 2
        if simple_number(i):
            result.append(i)
            print(i)


# task_12()

def task_13():
    user_input = int(input("String: "))
    user_input = str(user_input)
    index = 0

    result = None

    while index < len(user_input):
        result = user_input[::-1]
        index += 1

    print(result)


# task_13()

def task_14():
    def simple_number_check(n):
        for i in range(2, n + 1):
            if n == i:
                return True
            elif n % i == 0:
                return False
        return True

    user_input = int(input("Number: "))
    dauletsuper = user_input

    if not simple_number_check(user_input):
        if dauletsuper % 2 == 0:
            dauletsuper += 1
        else:
            dauletsuper += 2

    while True:
        if simple_number_check(dauletsuper):
            print(dauletsuper)
            break
        dauletsuper += 2


# task_14()


def task_15():
    user_string = str(input("String: "))
    user_input = int(input("Number: "))

    if user_string[0].isupper():
        user_string = user_string[0].lower() + user_string[1:]

    alphabet_dict = {}
    chishr = []

    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz', 1):
        alphabet_dict[letter] = i

    while True:
        for j in user_string:
            index = 0
            index = alphabet_dict[j]
            index += user_input
            if index > 26:
                index -= 26
            for key, value in alphabet_dict.items():
                if index == value:
                    chishr += key
                    break
        break
    for i in range(len(chishr)):
        print(chishr[i], end="")


# task_15()
