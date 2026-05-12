class Shape:
    def __init__(self):
        print("This is a shape.")
        

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        area = 3.14 * (radius ** 2)
        print(f"The area of the circle with radius {radius} is {area}.")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        area = length * width
        print(f"The area of the rectangle with length {length} and width {width} is {area}.")

circle1 = Circle(5)
rectangle1 = Rectangle(4, 6)

