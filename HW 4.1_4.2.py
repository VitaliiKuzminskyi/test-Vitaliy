
while True:
    try:
        a = float(input('Пожалуйста введите первое число: '))
        break
    except:
        print('Ввод символов кроме цифр ЗАПРЕЩЁН, введите первое число: ')

while True:
    try:
        b = float(input('Пожалуйста введите второе число: '))
        break
    except:
        print('Ввод символов кроме цифр ЗАПРЕЩЁН, введите второе число: ')

while True:
    try:
        c = float(input('Пожалуйста введите третье число: '))
        break
    except:
        print('Ввод символов кроме цифр ЗАПРЕЩЁН, введите третье число: ')

max = max(a, b, c)

if (a > 10 and b > 10 and c > 10) and ( a % 3 == 0 and b % 3 == 0): print (' Yes - Homework 3.1\n',max, '- Homework 3.2')

else: print(' No - Homework 3.1\n', max, '- Homework 3.2')