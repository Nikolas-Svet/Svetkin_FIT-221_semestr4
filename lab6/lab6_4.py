class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


# Пример использования
point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(5, 6)

print(point1 == point2)
print(point1 != point2)
print(point1 == point3)
print(point1 != point3)