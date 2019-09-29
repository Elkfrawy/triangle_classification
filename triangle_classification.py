ACCURACY = 10


def classify_triangle(a, b, c):
    """
    This function given a triangle three sides lengths, it classifies the triangle to be either
    scalene, isosceles, equilateral, or right triangle
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) \
            or not isinstance(c, (int, float)):
        raise NotATriangle("Invalid parameters. All sides must be numbers")

    if a >= b + c or b >= a + c or c >= a + b:
        raise NotATriangle("Invalid triangle, the sum of two sides must be more than the other side")

    if a == b and b == c:
        return [TriangleType.EQUILATERAL]

    result = []
    if a == b or b == c or a == c:
        result.append(TriangleType.ISOSCELES)

    # Check for right triangle
    a_square = a ** 2
    b_square = b ** 2
    c_square = c ** 2
    if almost_equals(a_square, b_square + c_square) or almost_equals(b_square, a_square + c_square)\
            or almost_equals(c_square, a_square + b_square):
        result.append(TriangleType.RIGHTTRIANGLE)

    # Any other case, it is scalene
    if len(result) == 0:
        return [TriangleType.SCALENE]

    return result


def almost_equals(num1, num2):
    """
    check whither both parameters as numbers are equals with precision of ACCURACY
    :param num1: first number
    :param num2: second number
    """
    return round(num1, ACCURACY) == round(num2, ACCURACY)


class NotATriangle(Exception):
    """
    This exception if a triangle sides lengths don't form a valid triangle
    """


class TriangleType:
    """
    An enum class for all different types of triangles
    """
    SCALENE = 'Scalene'
    ISOSCELES = 'Isosceles'
    EQUILATERAL = 'Equilateral'
    RIGHTTRIANGLE = 'RightTriangle'
