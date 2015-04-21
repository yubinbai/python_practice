def gcd(m, n):  # find the greatest common divisor
    while n:
        m, n = n, m % n
    return m


def gcd2(m, n):
    if n == 0:
        return m
    else:
        return gcd2(n, m % n)


def extended_gcd(a, b):
    '''
    return gcd, x0, y0
    for equation ax+by=g
    '''
    x, y = 0, 1
    lastx, lasty = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return a, lastx, lasty

if __name__ == '__main__':
    print extended_gcd(6, 4)
