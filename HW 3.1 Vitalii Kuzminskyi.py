
a = float(input('Пожалуйста введите первое число: ')) #использовал float для более широких возможностей и более точного расчёта
b = float(input('Пожалуйста введите второе число: '))
c = float(input('Пожалуйста введите третье число: '))

# def main():
#
#     a = True
#     while a:
#         a = False
#         float = input('Пожалуйста введите первое число: ')
#         try:
#             for i in float:
#                 if i.isdigit() is not True:
#                     raise ValueError("Первое число должно содержать только цифры")
#         except Exception:
#             print("Первое число должно содержать только цифры")
#             a = True
#
#
#
#     b = True
#     while b:
#         b = False
#         number2 = input('Пожалуйста введите второе число: ')
#         try:
#             for i in number2:
#                 if i.isdigit() is not True:
#                     raise ValueError("Второе число должно содержать только цифры")
#         except Exception:
#             print("Второе число должно содержать только цифры")
#             b = True
#
#     c = True
#     while c:
#         c = False
#         number3 = input('Пожалуйста введите третье число: ')
#         try:
#             for i in number3:
#                 if i.isdigit() is not True:
#                     raise ValueError("Третье число должно содержать только цифры")
#         except Exception:
#             print("Третье число должно содержать только цифры")
#             c = True
# if __name__ == '__main__':
#     main()



max = max(a, b, c)

if (a > 10 and b > 10 and c > 10) and ( a % 3 == 0 and b % 3 == 0): print (' Yes - Homework 3.1\n',max, '- Homework 3.2')

else: print(' No - Homework 3.1\n', max, '- Homework 3.2')