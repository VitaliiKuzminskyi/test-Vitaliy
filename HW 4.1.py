while True:
    try:
        base = int(input('Введите размер основания треугольника от 2 до 10: '))
        if 1 >= base or base > 10:
            pass
        else:
            break
    except:
        print('ОШИБКА ВВОДА!!! Ввод только цифр!')
n = base
a = '*'
b = '#'
print('\n' + 'HW 4.1')
for i in range(n, 0, -1):
    print(a * i)
print('HW 4.2', end='')
for i in range(0, (n + 1)):
    print(a * i)
print('HW 4.*1')

for i in range(0, (n + 1)):
    for j in range(n, (i + 1), -1):
        print((b * i) + (j * a))

        break





