from Childs import *
import pytest


def test_triangles():
    first_triangle = Triangles(3, 4, 5)
    assert first_triangle.perimetr() == 12
    assert first_triangle.square() == 6
    assert first_triangle.name == "Triangle"
    assert first_triangle.angles == 3


def test_rectangles():
    first_rectangle = Rectangles(5, 3)
    assert first_rectangle.perimetr() == 16
    assert first_rectangle.square() == 15
    assert first_rectangle.name == "Rectangle"
    assert first_rectangle.angles == 4


def test_quadrates():
    first_quadrate = Quadrates(6)
    assert first_quadrate.perimetr() == 24
    assert first_quadrate.square() == 36
    assert first_quadrate.name == "Quadrate"
    assert first_quadrate.angles == 4


def test_circles():
    first_circle = Circles(6)
    assert first_circle.perimetr() == 37.69911184307752
    assert first_circle.square() == 113.09733552923255
    assert first_circle.name == "Circle"
    assert first_circle.angles == 0


@pytest.mark.parametrize("params",
                         [{"obj": Triangles(8, 6, 10), "sum of sq": 30},
                          {"obj": Rectangles(5, 3), "sum of sq": 21},
                          {"obj": Quadrates(6), "sum of sq": 42},
                          {"obj": Circles(6), "sum of sq": 119.09733552923255},
                          ])
def test_add_square(params):
    first_obj = Triangles(3, 5, 4)
    second_obj = params["obj"]

    assert first_obj.add_square(second_obj) == params["sum of sq"]