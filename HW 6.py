                                                         # HW 6.1
print('HW 6.1 - Пользователь вводит слово, если это слово является полиндромом, то вывести "+", иначе "-"')
text1= input('Введите слово: ')
a = text1[0:]
b = text1[::-1]
if a == b\
    and not text1.isdigit() == True:
    print('Result HW 6.1: +\n')
else:
    print('Result HW 6.1: -\n')

                                                         # HW 6.2
print('HW 6.2 - Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести "YES", иначе "NO"')
text2_1 = input('Введите текст: ')
text2_2 = input('Введите слово: ')
a = text2_1.split()
if text2_2 in a\
    and not text2_2.isdigit() == True:
    print('Result HW 6.2: YES \n')
else:
    print('Result HW 6.2: NO \n')

                                                         # HW 6.3
print('HW 6.3 - Пользователь вводит строку. Если она начинается на "abc", то заменить их на www, иначе добавить в конец строки "zzz"')
text3 = input('Введите текст: ')
a = 'abc'
b = 'www'
c = 'zzz'
if text3.startswith(a) == True:
    print(f'Result HW 6.3: {text3.replace(a, b, 1)} \n')
else:
    print(f'Result HW 6.3: {text3 + c} \n')


                                                         # HW 6.4
print('HW 6.4 - Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю')
text4 = input('Введите текст: ')
words =[]
numbers = []
for i in text4:
    if i.isalpha():
        if not words or not last_isalpha:
            words.append(i)
        else:
            words[-1] += i
    else:
        if not numbers or last_isalpha:
            numbers.append(i)
        else:
            numbers[-1] += i
    last_isalpha = i.isalpha()
print(f'Result HW 6.4: {words} \n')

                                                        # HW 6.5
print('HW 6.5 - Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить, что в почте есть символ "@" и "." и если это так, то вывести YES, иначе NO')
text5 = input('Введите emal: ')
a = '@'
b = '.'
c = ' '
if text5.count(a) == 1\
        and text5.count(b) == 1\
            and text5.find(c) == -1:
    print('Result HW 6.5: YES \n')
else:
    print('Result HW 6.5: NO \n')