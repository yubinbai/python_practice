def reverse(s, start, end):
    original = list(s)
    mid = int((start + end) / 2 - start)
    for i in range(mid):
        swap = original[start + i]
        original[start + i] = original[end - i]
        original[end - i] = swap
    return ''.join(original)


def rotateRight(s, n):
    s = reverse(s, 0, len(s) - 1)
    s = reverse(s, 0, n - 1)
    s = reverse(s, n, len(s) - 1)
    return s


def rotateLeft(s, n):
    s = reverse(s, 0, len(s) - 1)
    s = reverse(s, len(s) - n, len(s) - 1)
    s = reverse(s, 0, len(s) - n - 1)
    return s

if __name__ == '__main__':
    original = 'abcdefghijk'
    print(original)
    print(reverse(original, 0, len(original) - 1))
    print(rotateRight(original, 3))
    print(rotateLeft(original, 3))
