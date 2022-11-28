                                        # HW 6.1
print('HW 6.1')
text1= input('Введите слово: ')
a = text1[0:]
b = text1[::-1]
if a == b:
    print('Result HW 6.1: +\n')
else:
    print('Result HW 6.1: -\n')

                                        # HW 6.2
print('HW 6.2')
text2_1 = input('Введите текст: ')
text2_2 = input('Введите слово: ')
if not text2_1.find(text2_2) == -1:
    print('Result HW 6.2: YES \n')
else:
    print('Result HW 6.2: NO \n')

                                        # HW 6.3
print('HW 6.3')
text3 = input('Введите текст: ')
a = text3.startswith('abc')
b = 'www'
c = 'zzz'
if a:
    print(f'Result HW 6.3: {b}{text3[3:]} \n')
else:
    print(f'Result HW 6.3: {text3}{c} \n')

                                        # HW 6.4
print('HW 6.4')
text4 = input('Введите текст: ')

