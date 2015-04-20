def swapBit(number, i, j):
    low = (number >> i) & 1
    high = (number >> j) & 1
    if low ^ high:
        mask = (1 << i) | (1 << j)
        number ^= mask
    return number

if __name__ == '__main__':
    n = int('1001010100001', 2)
    m = swapBit(n, 0, 6)
    print(bin(n))
    print(bin(m))
