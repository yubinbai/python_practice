from collections import namedtuple

Rectangle = namedtuple(
    'Rectangle', ['minX', 'maxX', 'minY', "maxY"], verbose=False)


def overlap(r1, r2):
    # 假定矩形是用一对点表达的(minx, miny) (maxx, maxy)，那么两个矩形
    # 相交的结果一定是个矩形，构成这个相交矩形rect{(minx, miny) (maxx, maxy)}的点对坐标是：
    minX = max(r1.minX, r2.minX)
    minY = max(r1.minY, r2.minY)
    maxX = min(r1.maxX, r2.maxX)
    maxY = min(r1.maxY, r2.maxY)
    return minX <= maxX and minY <= maxY

if __name__ == '__main__':
    r1 = Rectangle(0, 1, 0, 1)
    r2 = Rectangle(-1, 0, -1, 0)
    print overlap(r1, r2)
