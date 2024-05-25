class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
class Rectangle(Shape):
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * (self.width + self.length)
class Square(Shape):
    def area(self):
        return self.width * self.width
    def perimeter(self):
        return 4 * self.width
sum = Rectangle(5, 10)
total = Square(7, 7)

print(sum.area())
print(sum.perimeter())
print(total.area())
print(total.perimeter())