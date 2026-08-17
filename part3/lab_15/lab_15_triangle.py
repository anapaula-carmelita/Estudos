import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_point(self, point):
        return math.dist((point.getx(), point.gety()), (self.__x, self.__y))


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__a = vertice1
        self.__b = vertice2
        self.__c = vertice3

    def perimeter(self):
        dAB = self.__a.distance_from_point(self.__b)
        dBC = self.__b.distance_from_point(self.__c)
        dCA = self.__c.distance_from_point(self.__a)

        return dAB + dBC + dCA


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())