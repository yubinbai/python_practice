from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def signedArea2(p0, p1, p2):
    return p0.x * p1.y + p2.x * p0.y + p1.x * p2.y \
        - p2.x * p1.y - p0.x * p2.y - p1.x * p0.y


def area(p0, p1, p2):
    return 0.5 * abs(signedArea2(p0, p1, p2))
