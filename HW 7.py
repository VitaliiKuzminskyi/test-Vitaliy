                                                         # HW 7.1

print('HW 7.1 - Запросить у пользователя 5 чисел и записать их в список')

numbers = []
n = '5'
for i in range(5):
    number = input(f'Введите {n} чисел. Введите {i+1} число: ')
    if number.isdigit():
        numbers.append(number)


    else:
        break

print(f'Result HW 6.1: {numbers} \n')