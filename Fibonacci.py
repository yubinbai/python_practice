'''
differen ways to get the fib number
'''


def fib(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

for f in fib(2000000):
    print f,
print


def nthFib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for x in range(n - 2):
            a, b = b, a + b
        return b

fibs = []
for x in range(1, 40):
    if nthFib(x) < 20000000:
        fibs.append(nthFib(x))
print(fibs)


def fibRecursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibRecursive(n - 1) + fibRecursive(n - 2)

print(nthFib(10), fibRecursive(10))
