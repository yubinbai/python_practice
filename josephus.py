import math


def josephus(n, k):
    r = 0
    i = 2
    while i <= n:
        r = (r + k) % i
        i += 1
    return r + 1


def josephusPermutation(n, k):
    current = list(range(1, n + 1))
    idx = -1
    remains = n
    while (remains >= 1):
        idx = (idx + k) % len(current)
        yield current[idx]
        del current[idx]
        remains -= 1
        idx -= 1

print josephus(6, 5)
print list(josephusPermutation(6, 5))
