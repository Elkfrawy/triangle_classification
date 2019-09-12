ACCURACY = 10

def classify_triangle(a, b, c):
    """
    This function given a triangle three sides lengths, it classifies the triangle to be either scalene, isosceles, equilateral, or right triangle
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)) :
        raise NotATriangle("Invalid parameters. All sides must be numbers")

    if a >= b + c or b >= a + c or c >= a + b:
        raise NotATriangle("Invalid triangle, the sum of two sides must be more than the other side")

    if a == b and b == c:
        return [TriangleType.EQUILATERAL]

    result = []
    if a == b or b == c:
        result.append(TriangleType.ISOSCELES)

    # Check for right triangle
    a2 = a ** 2
    b2 = b ** 2
    c2 = c ** 2
    if almost_equals(a2, b2 + c2) or almost_equals(b2, a2 + c2) or almost_equals(c2, a2 + b2):
        result.append(TriangleType.RIGHTTRIANGLE)

    # Any other case, it is scalene
    if len(result) == 0:
        return [TriangleType.SCALENE]
    else:
        return result


def almost_equals(x, y):
    return round(x, ACCURACY) == round(y, ACCURACY)


class NotATriangle(Exception):
    pass


class TriangleType(object):
    SCALENE = 'Scalene'
    ISOSCELES = 'Isosceles'
    EQUILATERAL = 'Equilateral'
    RIGHTTRIANGLE = 'RightTriangle'

