#
#                                                          # HW9_1
#
# print('HW 9.1')
# hw9_1 = open('hw9_1.txt', 'r')
# text = hw9_1.read()
#
# words = []
# numbers = []
# for i in text:
#     if i.isnumeric():
#         if not numbers or not last_isnumeric:
#             numbers.append(i)
#         else:
#             numbers[-1] += i
#     else:
#         if not words or last_isnumeric:
#             words.append(i)
#         else:
#             words[-1] += i
#     last_isnumeric = i.isnumeric()
# print(numbers)

#                                                          # HW9_2
#
# print('HW 9.2')
# hw9_2 = open('data_hw9_2.txt', 'w')
# hw9_2.write(input('Введите текст для записи в файл: '))
#
#                                                          # HW9_3
#
# print('HW 9.3')
# while True:
#     try:
#         n = int(input('Введите количество чисел: '))
#         break
#     except:
#         print('ОШИБКА!!! Ввод только целых чисел: ')
#
# rec_numbers = []
# symbol = ' '
# for i in range(n):
#     f = input(f'Из {n} чисел введите {i+1} число: ')
#     rec_numbers.append(f)
#
# hw9_3_done = (symbol.join(rec_numbers))
# hw9_3 = open('hw9_3_numbers.txt', 'w')
# hw9_3.write(hw9_3_done)

#                                                          # HW9_4
#
# print('HW 9.4')
# import random
# numbers = []
# file9_4 =  open('hw9_4_numbers.txt', 'w')
# n = 100
# a = '\n'
# for i in range(n):
#     k = random.randint(0, 200)
#     s = str(k)
#     numbers.append(s)
#     file9_4.write(s + a)
#
#                                                          # HW9_5
# print('HW 9.5')
# hw9_5 = open('HW9_5.txt', 'r')
# text = hw9_5.read()
#
# words = []
# numbers = []
# for i in text:
#     if i.isnumeric():
#         if not numbers or not last_isnumeric:
#             numbers.append(i)
#         else:
#             numbers[-1] += i
#     else:
#         if not words or last_isnumeric:
#             words.append(i)
#         else:
#             words[-1] += i
#     last_isnumeric = i.isnumeric()
#
# print(words)
# print(len(words))




