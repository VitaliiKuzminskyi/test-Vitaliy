
number = int(input('Пожалуйста введите целое трёхзначное число: '))

if 100 <= number <= 999:
    reversed_number = 0
    while number > 0:
        z = number % 10
        number //= 10
        reversed_number *= 10
        reversed_number += z
    print(reversed_number)


else:
    print('No')
