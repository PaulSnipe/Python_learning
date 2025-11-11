# Симулятор сюрприза(при запуске отображается один из 5 различных выриантов)
def surprice():
    import random
    num = random.randint(1, 5)
    print(num)
# Подбрасывание монеты 100 раз и пишет сколько орел или решка
def coin():
    import random
    heads = 0
    tails = 0
    for i in range(1, 101):
        brosok = random.randint(0,1)
        if brosok == 0:
            heads += 1
        else:
            tails += 1
    print(f'орел выпал {heads} раз, а решка - {tails} ')

# Программа отгадай число
def number():
    import random
    num = random.randint(1, 100)
    quess = int(input('Введите число: '))
    tries = 1 # число попыток
    max_tries = 3
    while quess != num and tries < max_tries:
        if quess > num:
            print('Меньше')
        else:
            print('больше')
        quess = int(input('Ваше предположение: '))
        tries += 1
    if quess == num:
        print(f'Вы отгадали число {num}, затратив {tries} попыток')
    else:
        print(f'Слишком много попыток')
# пример бинарного поиска
def bin_poisk():
    print('Загадываем число от 1 до 100')
    num = int(input())
    low = 1
    high = 100
    attempts = 0
    found = False
    while not found:
        quess = (low + high)//2
        attempts += 1
        print(f'моя догадка {quess}')
        feedback = input("Введите '<', '>' или '=' ")
        if feedback == "=":
            print(f'угадал число {num} за {attempts} попыток ')
        elif feedback == "<":
            high = quess - 1
        elif feedback == ">":
            low = quess + 1
        else:
            print('неправильный символ')
