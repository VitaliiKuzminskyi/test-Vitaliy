
while True:
    try:
        number = int(input('Пожалуйста введите целое трёхзначное число: '))
        break
    except:
        print('Ввод символов кроме цифр ЗАПРЕЩЁН, введите трёхзначное число: ')

if 100 <= number <= 999:
    a = 0
    while number > 0:
        z = number % 10
        number //= 10
        a *= 10
        a += z

    reversed_number = a

print(reversed_number)
