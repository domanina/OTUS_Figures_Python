from Base_Figure import Figure


class Triangles(Figure):
    def __init__(self, a, b, c):
        self.name = "Triangle"
        self.angles = 3
        self.a = a
        self.b = b
        self.c = c
        self.per = self.perimetr()
        self.sq = self.square()
        super().__init__()
        print("=====================================")


class Rectangles(Figure):
    def __init__(self, a, b):
        self.name = "Rectangle"
        self.angles = 4
        self.a = a
        self.b = b
        self.per = self.perimetr()
        self.sq = self.square()
        super().__init__()
        print("=====================================")


class Quadrates(Figure):
    def __init__(self, a):
        self.name = "Quadrate"
        self.angles = 4
        self.a = a
        self.per = self.perimetr()
        self.sq = self.square()
        super().__init__()
        print("=====================================")


class Circles(Figure):
    def __init__(self, r):
        self.name = "Circle"
        self.angles = 0
        self.r = r
        self.per = self.perimetr()
        self.sq = self.square()
        super().__init__()
        print("=====================================")







