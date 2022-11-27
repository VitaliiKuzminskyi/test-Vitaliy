while True:
    try:
        base = int(input('Введите размер основания треугольника от 2 до 10: '))
        if 1 >= base or base > 10:
            pass
        else:
            break
    except:
        print('ОШИБКА ВВОДА!!! Ввод только цифр!')
print(f'Yes {base}')
