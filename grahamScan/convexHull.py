'''
Created on Jun 21, 2013
@author: Yubin Bai
All rights reserved.
'''
from collections import namedtuple
from math import atan2
from random import randrange
from matplotlib import pyplot

Point = namedtuple('Point', ['x', 'y'])


def ccw(p, q, r):
    '''
    CCW (Counter Clockwise) Test
    '''
    def turn(p, q, r):
        '''
        application of cross product
        '''
        x1, y1 = q.x - p.x, q.y - p.y  # vector p->q
        x2, y2 = r.x - q.x, r.y - q.y  # vector q->r
        result = x1 * y2 - x2 * y1  # 1 cross 2
        if result < 0:
            return -1  # P->Q->R is a right turn
        if result > 0:
            return 1  # P->Q->R is a left turn (counter )
        return 0  # P->Q->R is a straight line, i.e. P, Q, R are collinear
    return (turn(p, q, r) > 0)


def area2(a, b, c):
    return a.x * b.y - a.y * b.x + b.x * c.y - b.y * c.x + c.x * a.y - c.y * a.x


def grahamstackearch(polygon):
    def pivotAngle(a):
        d1x = a.x - pivot.x
        d1y = a.y - pivot.y
        return atan2(d1y, d1x)

    # first, find P0 = point with lowest Y and if tie: rightmost X
    p0 = 0
    N = len(polygon)
    for i in range(N):
        if polygon[i].y < polygon[p0].y or\
                (polygon[i].y == polygon[p0].y and polygon[i].x > polygon[p0].x):
            p0 = i
    polygon[0], polygon[p0] = polygon[p0], polygon[0]
    # second, sort points by angle w.r.t. P0, skipping Polygon [0]
    pivot = polygon[0]  # use this global variable as reference
    polygon = [polygon[0]] + sorted(polygon[1:], key=pivotAngle)

    # third, the ccw tests
    # put two starting vertices into stack
    stack = [polygon[N - 1], polygon[0]]
    i = 1  # and start checking the rest
    while (i < N):  # note: N must be >= 3 for this method to work
        now = stack[-1]
        prev = stack[-2]
        # if these 3 points make a left turn
        if (ccw(prev, now, polygon[i])):
            stack.append(polygon[i])
            i += 1
        else:
            stack.pop()
    # the last point is a duplicate of first point
    return stack


def isInside(pt, poly):
    for i in range(1, len(poly)):
        if not ccw(pt, poly[i - 1], poly[i]):
            return False
    return True


def polyArea(poly):
    return 0.5 * sum([poly[i - 1].x * poly[i].y - poly[i].x * poly[i - 1].y for i in range(1, len(poly))])

if __name__ == '__main__':
    maxN = 20
    maxLimit = 1000

    polygon = []
    for i in range(maxN):
        x = randrange(-1 * maxLimit, maxLimit)
        y = randrange(-1 * maxLimit, maxLimit)
        polygon.append(Point(x, y))

    xList = [p.x for p in polygon]
    yList = [p.y for p in polygon]
    pyplot.scatter(xList, yList)

    hull = grahamstackearch(polygon)
    xList = [p.x for p in hull]
    yList = [p.y for p in hull]
    pyplot.plot(xList, yList)

    pyplot.show()
