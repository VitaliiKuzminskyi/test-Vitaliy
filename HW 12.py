def is_two(n):
    while n != 1 and n / 2 != 1:
        n = n - (n / 2)
        if n == int(n):
            continue
        elif n != int(n):
            print('No')
            break
    if n / 2 == 1 or n == 1:
        print('Yes')

is_two(int(input('Введите проверяемое число: ')))