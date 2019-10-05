"""
Class
===============================================
Numbers, String, Boolean : is class, but shopping card is not class or any type. So we need to create one type using class.
List, Dictionaries : is also class
Self : is refernce of current object
"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)


"""
Inheritance
===============================================
"""


class Line(Point):
    def __init__(self):
        pass

    def test(self):
        print("test method")


line = Line()
line.test()
