def reverse(s):
    target = list(s)
    for i in range(int(len(s) / 2)):
        swap = target[i]
        target[i] = target[len(s) - i - 1]
        target[len(s) - i - 1] = swap
    return ''.join(target)

if __name__ == '__main__':
    s = 'abcdef'
    print(reverse(s))
    print(s[::-1])
