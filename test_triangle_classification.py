from math import sqrt

import pytest
from triangle_classification import classify_triangle, NotATriangle, TriangleType

def test_raises_exception_not_triangle():
    with pytest.raises(NotATriangle):
        classify_triangle(5, 1, 2)

def test_raises_exception_not_triangle_oneside_equal_to_sum_of_the_others():
    with pytest.raises(NotATriangle):
        classify_triangle(6, 3, 3)

def test_raises_exception_not_triangle_oneside_equal_to_sum_of_the_others_float():
    with pytest.raises(NotATriangle):
        classify_triangle(2.0000000000000000000000002, 1.0000000000000000000000001, 1.0000000000000000000000001)

def test_raises_exception_zeros():
    with pytest.raises(NotATriangle):
        classify_triangle(0, 0, 0)

def test_raises_exception_string_number_side():
    with pytest.raises(NotATriangle):
        classify_triangle('5', 10, 7)

def test_raises_exception_string_number_side2():
    with pytest.raises(NotATriangle):
        classify_triangle(5, '10', 7)

def test_raises_exception_string_number_side3():
    with pytest.raises(NotATriangle):
        classify_triangle(5, 7, '10')

def test_raises_exception_string_number_sides():
    with pytest.raises(NotATriangle):
        classify_triangle('10', '15', '20')

def test_raises_exception_string_char_side():
    with pytest.raises(NotATriangle):
        classify_triangle('abc', 0, 0)

def test_raises_exception_any_zero():
    with pytest.raises(NotATriangle):
        classify_triangle(0, 1, 2)

def test_classify_equilateral_triangle_integer():
    assert classify_triangle(5, 5, 5) == [TriangleType.EQUILATERAL]

def test_classify_equilateral_triangle_float():
    assert classify_triangle(10.2, 10.2, 10.2) == [TriangleType.EQUILATERAL]

def test_classify_isosceles_integer():
    assert classify_triangle(5, 5, 7) == [TriangleType.ISOSCELES]

def test_classify_isosceles_integer2():
    assert classify_triangle(5, 7, 5) == [TriangleType.ISOSCELES]

def test_classify_isosceles_integer3():
    assert classify_triangle(7, 5, 5) == [TriangleType.ISOSCELES]

def test_classify_right_triangle():
    assert classify_triangle(3, 4, 5) == [TriangleType.RIGHTTRIANGLE]

def test_classify_right_triangle2():
    assert classify_triangle(3, 5, 4) == [TriangleType.RIGHTTRIANGLE]

def test_classify_right_triangle3():
    assert classify_triangle(5, 3, 4) == [TriangleType.RIGHTTRIANGLE]

def test_classify_right_isosceles_triangle():
    assert set(classify_triangle(1, 1, sqrt(2))) == {TriangleType.ISOSCELES, TriangleType.RIGHTTRIANGLE}

def test_classify_right_triangle_big_numbers():
    assert classify_triangle(3*99**100, 4*99**100, 5*99**100) == [TriangleType.RIGHTTRIANGLE]

def test_classify_scalene_triangle():
    assert classify_triangle(4, 7, 9) == [TriangleType.SCALENE]
