'''
Created on Jun 21, 2013

@author: Yubin Bai

All rights reserved.
'''
from collections import namedtuple
from random import randrange

Point = namedtuple('Point', ['x', 'y'])


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def turn(p, q, r):
    '''
    application of cross product
    '''
    x1, y1 = q.x - p.x, q.y - p.y  # vector p->q
    x2, y2 = r.x - q.x, r.y - q.y  # vector q->r

    result = x1 * y2 - x2 * y1  # 1 cross 2
    if result < 0:
        return 1  # P->Q->R is a right turn
    if result > 0:
        return -1  # P->Q->R is a left turn
    return 0  # P->Q->R is a straight Line, i.e. P, Q, R are collinear


def ccw(p, q, r):
    '''
    CCW (Counter Clockwise) Test
    '''
    return int(turn(p, q, r) > 0)


def linesIntersect(line1, line2):
    return ((ccw(line1.p1, line1.p2, line2.p1) * ccw(line1.p1, line1.p2, line2.p2)) <= 0) \
        and \
        ((ccw(line2.p1, line2.p2, line1.p1) * ccw(line2.p1, line2.p2, line1.p2)) <= 0)


def isParallel(line1, line2):
    # cross product equals zero
    if ((line1.p2.x - line1.p1.x) * (line2.p2.y - line2.p1.y) - (line2.p2.x - line2.p1.x) * (line1.p2.y - line1.p1.y)) == 0:
        return True
    return False

if __name__ == '__main__':
    maxN = 4
    maxLimit = 10

    polygon = []
    for i in range(maxN):
        x = randrange(-1 * maxLimit, maxLimit)
        y = randrange(-1 * maxLimit, maxLimit)
        polygon.append(Point(x, y))
        print(x, y)

    p1, p2, p3, p4 = polygon

    line1 = Line(p1, p3)
    line2 = Line(p2, p4)

    print(linesIntersect(line1, line2))
    print(isParallel(line1, line2))
