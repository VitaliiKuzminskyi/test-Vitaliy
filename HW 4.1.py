base = input('Введите размер основания треугольника от 2 до 10: ')
if base.isdigit() and len(base) == 1:
    base = int(base)
    if ( 1 < base, base < 10):
         print(f'Ширина = {base}')
    else:
        print('Ошибка')
#     # print(number[::-1])
#
#     first_digit = number // 100  # 1
#     second_digit = number % 100 // 10  # 2
#     third_digit = number % 10  # 3
#
#     reversed_number = third_digit * 100 + second_digit * 10 + first_digit
#     print(reversed_number)
# else:
#     print('Error')






# while True:
#     try:
#         base = int(input('Введите размер основания треугольника от 2 до 10: ') and len(base) ==2)
#         break
#     except:
#         print('Ошибка!!! Ввод только цифр от 2 до 10')
#
#
#
# else:
#     print('No ')
