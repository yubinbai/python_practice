def countBits(n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c

if __name__ == '__main__':
    print countBits((1 << 31) - 1)
    print countBits((1 << 31) - 1 - (1 << 10) - (1 << 11))