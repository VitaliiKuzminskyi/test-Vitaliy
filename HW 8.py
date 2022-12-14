
                                                         HW 8.1
print('HW 8.1')
a = {'Dmitriy', 'Nikolay', 'Vasyliy', 'Tatyana', 'Masha', 'Natasha'}
b = {'Anton', 'Dmitriy', 'Vladimir', 'Alexey', 'Masha', 'Natasha', 'Olga'}
print(f' За сентябрь и октябрь должны: { sorted(a.union(b))}, \n Только за октябрь должны: { sorted(b.difference(a))}')

                                                         # HW 8.2
print('HW 8.2')
while True:
    try:
        n = int(input('Введите количество повреждённых файлов: '))
        break
    except:
        print('ОШИБКА!!! Ввод только целых чисел: ')


print('Действия с файлами:\n R - чтение; \n W - запись; \n E - выполненение.')
permissions = {}
for i in range(n):
    f = input(f'Из {n} файлов введите имя {i+1}-го файла и действия с ним (например readme.txt R W): ').split()
    permissions[f[0]] = set(f[1:])


for j in range(int(input('Введите количество действий над файлами: '))):
        permis, file = input('Запросите действие (read/write/execute) над файлом и его имя (например: read [имя файла]): ').split()
        if permis == 'read':
            permis = 'R'
        if permis == 'write':
            permis = 'W'
        if permis == 'execute':
            permis = 'E'
        if permis in permissions[file]:
            print('OK')
        else:
            print('Access denied')