a = int(input('Введите минуту: '))
b = 59


if 0 <= a <= (b / 4):
    print('First')
elif (b / 4) <= a <= (b / 2):
    print('Second')
elif (b / 2) <= a <= ( (3 * b) / 4):
    print('Third')
elif ( (3 * b) / 4) <= a <= b:
    print('Fourth')

else:
    print('Error')