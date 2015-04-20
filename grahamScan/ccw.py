from collections import namedtuple

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
            return 1  # P->Q->R is a left turn
        return 0  # P->Q->R is a straight line, i.e. P, Q, R are collinear
    return (turn(p, q, r) > 0)

if __name__ == '__main__':
    p = Point(1, 2)
    q = Point(2, 4)
    r = Point(3, 6)
    r1 = Point(3, 7)
    r2 = Point(3, 5)
    print(ccw(p, q, r))
    print(ccw(p, q, r1))
    print(ccw(p, q, r2))
