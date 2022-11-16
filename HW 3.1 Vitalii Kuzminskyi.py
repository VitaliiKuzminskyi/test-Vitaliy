# HW 3.1-3.2


a = float(input('Пожалуйста введите первое число: ')) #использовал float для более широких возможностей и более точного расчёта
b = float(input('Пожалуйста введите второе число: '))
c = float(input('Пожалуйста введите третье число: '))

max = max(a, b, c)

if (a > 10 and b > 10 and c > 10) and ( a % 3 == 0 and b % 3 == 0): print (' Yes - Homework 3.1\n',max, '- Homework 3.2')

else: print(' No - Homework 3.1\n', max, '- Homework 3.2')