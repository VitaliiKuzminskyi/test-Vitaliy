
                                                         # HW10_1
list = [ 1, 2, 3, 4 ]
def change(list):
    list[0], list[-1] = list[-1], list[0]
    return
change(list)
print(f' HW10.1: {list}')

                                                         # HW10_2

def to_dict(list):
    return {element: element for element in list}
# print(to_dict([list]))
print(f' HW10.2:', to_dict([1, 2, 'One', 'Two']) )

                                                         # HW10_3

while True:
    try:
        start = int(input('Введите первое число: '))
        break
    except:
        print('ОШИБКА ВВОДА!!! Ввод только целых чисел!')

while True:
    try:
        end = int(input('Введите второе число: '))
        break
    except:
        print('ОШИБКА ВВОДА!!! Ввод только целых чисел!')

def sum_range(start, end):
    if end < start:
        return sum(range(end, start + 1))
    else:
        return sum(range(start, end+1))
print(f'HW10.3: Сумма всех чисел от {start} до {end} = ', sum_range(start, end))

#                                                          # HW10_4
#
while True:
    try:
        lines = int(input('Укажите количество последних строк которые нужно вывести: '))
        if lines > 0:
            break
        else:
            print('ОШИБКА ВВОДА!!! Ввод только целых чисел больше нуля!')
    except:
        print('ОШИБКА ВВОДА!!! Ввод только целых чисел!')
ends = '.txt'
file = input('Укажите имя файла : ')
if file.endswith(ends) == True:
    filename = file
else:
    filename = file + ends


def read_last(lines, file):
    with open(file, encoding='utf-8') as text:
        file_lines = text.readlines()[-lines:]
    for line in file_lines:
            print(line.strip())
    return
read_last(lines, filename)

