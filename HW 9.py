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
#
# hw9_5 = open('HW9_5.txt', 'r')
# text = hw9_5.read()
# words = text.split()
# print(f'HW 9.5 В тексте {len(words)} слов')
#
#                                                          # HW9_6
#
# print('HW 9.6')
# hw9_6 = open('HW9_6.txt', 'r')
# text = hw9_6.read()
# numbers = text.split()
# num = []
# for i in numbers:
#     if i.isdigit():
#         s = int(i)
#         num.append(s)
# print(sum(num))

#                                                          # HW9_7
'''
Дан файл в котором записан текст, необходимо вывести топ 5 слов которые чаще всего повторяются, пример:
в - 20 раз
привет - 10 раз
как - 9 раз
у - 7
world - 4
'''
print('HW 9.7')
from collections import Counter
hw9_7 = open('9_7.txt', 'r', encoding='utf-8')
text = hw9_7.read()

word_list = []

for word in text.split():
    clear_word = ''
    for letter in word:
        if letter.isalpha():
            clear_word += letter.lower()
    word_list.append(clear_word)
print(Counter(word_list), '\n')
print(*sorted(set(word_list), key=word_list.count, reverse=True)[:5], sep='\n')


