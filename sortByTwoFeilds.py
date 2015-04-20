class Struct(object):

    """docstring for Struct"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        # a by increasing, b by decreasing
        if self.a < other.a:
            return 1
        elif self.a > other.a:
            return 0
        else:
            return self.b > other.b

    def __str__(self):
        return '(%d, %d)' % (self.a, self.b)

import random
if __name__ == '__main__':
    a = [Struct(random.randrange(1, 10), random.randrange(1, 100))
         for _ in range(10)]
    for w in a:
        print w,
    a.sort()
    print
    for w in a:
        print w,
