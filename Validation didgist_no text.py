while True:
    try:
        number = int(input('Введите размер основания треугольника от 2 до 10: '))
        if 1 >= number or number > 10:
            pass
        else:
            break
    except:
        print('ОШИБКА ВВОДА!!! Ввод только цифр!')

print(f'Yes {number}')
