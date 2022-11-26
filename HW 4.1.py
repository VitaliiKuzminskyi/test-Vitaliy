
# base_size = input('Enter triangle\'s base size (2-10): ')
# if base_size.isdigit() and 2<=base_size<=10:
#     n=int(base_size)
#     print(n)
#
# else:
#     input('Pleace use only didgists input (2-10): ')

base_number = int
base_number = input('Enter triangle\'s base size (2-10): ')
while base_number.isdigit():
    n=int(base_number)
    if 2<=n<=10: print(f'Ok Base = {n}')
    break

else:
        input('Pleace use only didgists input (2-10): ')


# base_size = int
# while True:
#     try:
#         int(input(base_size := 'Enter triangle\'s base size (2-10): '))
#         break
#     except:
#         print('WARNING!!! Only didgits input!')
#
# if (1 < base_size < 11): print('Ok')
