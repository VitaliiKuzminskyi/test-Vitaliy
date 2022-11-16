# HW 3.1

a = float(input('Пожалуйста введите первое число: '))
b = float(input('Пожалуйста введите второе число: '))
c = float(input('Пожалуйста введите третье число: '))
g= a, b, c
#print('Yes'if ((a, b, c) > 10) else  'No')
print('Yes'if g > 10 else 'No')