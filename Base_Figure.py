import math


class Figure():
    def __init__(self):
        self.name
        self.angles
        self.per
        self.sq
        self.print_name_and_angles()

    def print_name_and_angles(self):
        print(self.name)
        print("I have ", self.angles, " angles")

    def perimetr(self):
        if self.name == "Triangle":
            per = self.a + self.b + self.c

        elif self.name == "Rectangle":
            per = 2 * (self.a + self.b)

        elif self.name == "Quadrate":
            per = 4 * self.a

        elif self.name == "Circle":
            per = 2 * self.r * math.pi

        else:
            print ("any perimetr")

        if (per is not None):
            print("My perimetr is ", per)
            return per


    def square(self):
        if self.name == "Triangle":
            half_per=self.per/2
            square = math.sqrt(half_per * (half_per - self.a) * (half_per - self.b) * (half_per - self.c))

        elif self.name == "Rectangle":
            square = self.a*self.b

        elif self.name == "Quadrate":
            square = self.a**2

        elif self.name == "Circle":
            square = math.pi * (self.r**2)

        else:
            print ("any square")

        if (square is not None):
            print("My square is ", square)
            return square



    def add_square(self, obj):
        sum_of_squares = self.sq + obj.sq
        print("Sum for two figures = ", sum_of_squares)
        print("=====================================")
        return sum_of_squares


















