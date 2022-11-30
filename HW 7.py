                                                         # HW 7.1
# print('HW 7.1 - Запросить у пользователя 5 чисел и записать их в список')
# numbers = []
# n = 5
# while True:
#     try:
#         for i in range(0, n):
#             number = int(input(f'Введите {n} чисел. Введите {i + 1} число: '))
#             numbers.append(number)
#         break
#     except:
#         print(f'Ввод символов кроме цифр ЗАПРЕЩЁН!!! Введите {n} чисел. Введите {i + 1} число: : ')
#         # number = int(input(f'Введите {n} чисел. Введите {i + 1} число: '))
# print(f'Result HW 7.1: {numbers} \n')

                                                         # HW 7.2

# print('HW 7.2 - Дан список A = [1, 2, 3, 4, 5] Удалить последнее число из списка')
# list2 = ['1', '2', '3', '4', '5']
# a = list2[-1]
# list2.remove(a)
# print(f'Result HW 7.2: {list2} \n')

                                                         # HW 7.3
print('HW 7.3 - Запросить у пользователя 10 чисел и записать их в список A\n'
      'Запросить у пользователя число N\n'
      'Вывести пользователю сколько в списке A повторяется число N')

numbers = []
a = 3
while True:
    try:
        for i in range(0, a):
            number = int(input(f'Введите {a} чисел. Введите {i + 1} число: '))
            numbers.append(number)
        break
    except:
        print(f'Ввод символов кроме цифр ЗАПРЕЩЁН!!! Введите {a} чисел. Введите {i + 1} число: : ')

while True:
    try:
        n = int(input('Введите искомое число: '))
        break
    except:
        print(f'Искомое число не может быть не цифрой:')
b = numbers.count(n)
print(f'Result HW 7.3. В Вашем списке {b} искомых \'{n}\' \n')


