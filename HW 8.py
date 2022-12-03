                                                         # HW 8.1
print('HW 8.1')
a = {'Dmitriy', 'Nikolay', 'Vasyliy', 'Tatyana', 'Masha', 'Natasha'}
b = {'Anton', 'Dmitriy', 'Vladimir', 'Alexey', 'Masha', 'Natasha', 'Olga'}
print(f' За сентябрь и октябрь должны: { sorted(a.union(b))}, \n Только за октябрь должны: { sorted(b.difference(a))}')


