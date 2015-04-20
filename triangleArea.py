class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		

def signedArea2(p0, p1, p2):
	# cross product
    return p0.x * p1.y + p2.x * p0.y + p1.x * p2.y \
        - p2.x * p1.y - p0.x * p2.y - p1.x * p0.y


def area(p0, p1, p2):
    return 0.5 * abs(signedArea2(p0, p1, p2))

if __name__ == '__main__':
	p1 = Point(0, 0)
	p2 = Point(3, 0)
	p3 = Point(0, 4)
	print signedArea2(p1, p2, p3)
	print area(p1, p2, p3)
