class Shape:
    def draw(self):
        pass

class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width
        for i in range(1, width + 1):
            print('*' * i)

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        print(('*' * width + '\n') * height)


print('HW 14.1:')
one = Triangle(3)

print('HW 14.2:')
two = Rectangle(6, 3)






