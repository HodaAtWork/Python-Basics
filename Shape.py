#
# Voorbeeld ter oefening van Class
#
class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
        self.coll = []

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

    def addCollection(self, value):
        self.coll.append(value)

    def collection(self):
        return self.coll

#
# Voorbeeld inheritance
#
class Square(Shape):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.description = "een vierkant"

#
# Double square met y = |
#  ____ ____
# |____|____|
# 
class DoubleSquare(Square):
    def __init__(self, y):
        self.x = 2 * y
        self.y = y
        self.description = "een dubbel vierkant"

    def perimeter(self):
        return 3 * self.y + 2 * self.x

