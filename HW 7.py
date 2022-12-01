                                                         # HW 7.1

print('HW 7.1')
numbers = []
n = 5

while True:
    try:
        for i in range(0, n):
            number = float(input(f'Введите {i + 1} число из {n}: '))
            numbers.append(number)
        break
    except:
        print(f'Ввод символов кроме цифр ЗАПРЕЩЁН!!! Введите {i + 1} число из {n}: ')
        numbers.clear()

print(f'Result HW 7.1: {numbers} \n')

                                                         # HW 7.2

print('HW 7.2')
list2 = [1, 2, 3, 4, 5]
a = list2[-1]
list2.remove(a)
print(f'Result HW 7.2: {list2} \n')

                                                         # HW 7.3

print('HW 7.3')
numbers = []
a = 10

while True:
    try:
        for i in range(0, a):
            number = float(input(f'Введите {i + 1} число из {a}: '))
            numbers.append(number)
        break
    except:
        print(f'Ввод символов кроме цифр ЗАПРЕЩЁН!!! Введите {i + 1} число из {a}: ')
        numbers.clear()

while True:
    try:
        n = float(input('Введите искомое число: '))
        break
    except:
        print(f'Искомое число должно состоять из цифр: ')

b = numbers.count(n)
print(f'Result HW 7.3. В Вашем списке {b} искомых \'{n}\' \n')

                                                         # HW 7.4

print('HW 7.4')

while True:
    try:
        n = int(input('Количество чисел в списке: '))
        break
    except:
        print(f'Ввод только цифр: ')

numbers = []
while True:
    try:
        for i in range(0, n):
            number = float(input(f'Введите {i + 1} число из {n}: '))
            numbers.append(number)
        break
    except:
        print(f'Ввод символов кроме цифр ЗАПРЕЩЁН!!! Введите {i + 1} число из {n}: ')
        numbers.clear()

numbers.reverse()
print(f'Result HW 7.4. Ваши числа в обратном порядке: {numbers} \n')

                                                         # HW 7.5

print('HW 7.5')
numbers = []
n = 5

while True:
    try:
        for i in range(0, n):
            number = float(input(f'Введите {i + 1} число из {n}: '))
            numbers.append(number)
        break
    except:
        print(f'Ввод символов кроме цифр ЗАПРЕЩЁН!!! Введите {i + 1} число из {n}: ')
        numbers.clear()

c = []
for i in numbers:
    if i > 5:
        c.append(i)
print(f'Result HW 7.5:Числа > 5 в списке C: {c} \n')

                                                         # HW 7.6

print('HW 7.6')
numbers = []
while True:
    try:
        n = int(input('Количество чисел в списке: '))
        break
    except:
        print(f'Ввод только целых чисел: ')

while True:
    try:
        for i in range(0, n):
            number = int(input(f'Введите {i + 1} число из {n}: '))
            numbers.append(number)
        break
    except:
        print(f'Ввод символов кроме цифр ЗАПРЕЩЁН!!! Введите {i + 1} число из {n}: ')
        numbers.clear()

mins = numbers[0]
for i in numbers[1::]:
    if i < mins:
        mins = i

maxs = numbers[0]
for i in numbers[1::]:
    if i > maxs:
        maxs = i

print(f'Result HW 7.6 Минимальное число: {mins}, максимальное число: {maxs}\n')

                                                         # HW 7.7

print('HW 7.7')
text7 = input('Введите текст: ')
words = []
numbers = []
for i in text7:
    if i.isnumeric():
        if not numbers or not last_isnumeric:
            numbers.append(i)
        else:
            numbers[-1] += i
    else:
        if not words or last_isnumeric:
            words.append(i)
        else:
            words[-1] += i
    last_isnumeric = i.isnumeric()

n = len(numbers)

print(f'Result HW 7.7: {n} \n')