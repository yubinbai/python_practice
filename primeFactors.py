import math


def primeFactors(n):
    '''
    lists prime factors of a natural number, from greatest to smallest
    '''
    i = 2
    result = []
    while i <= math.sqrt(n):
        while n % i == 0:
            result.append(i)
            n /= i
        i += 1
    if n != 1:
        result.append(n)
    result.sort()
    return result


def primeFactorsRecur(n):
    '''
    lists prime factors of a natural number, from greatest to smallest
    '''
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            l = primeFactorsRecur(n / i)
            l.append(i)
            return l
        i += 1
    return [n]  # n is prime


def primeFactors2(n):
    '''
    lists prime factors of a natural number, from greatest to smallest
    '''
    i = 2
    flag = False
    while i <= math.sqrt(n):
        if n % i == 0:
            flag = True
            break
        i += 1
    if flag:
        iCounter = 0
        while not n % i:
            iCounter += 1
            n //= i
        if n != 1:
            l = primeFactors(n)
            l.extend([i] * iCounter)
            return l
        else:
            return [i] * iCounter
    else:
        return [n]  # n is prime


if __name__ == '__main__':
    for number in range(2, 1000000):
        a = primeFactors(number)
        a.sort()
        b = primeFactorsRecur(number)
        b.sort()
        if not b == a:
            print 'false'
            break
    print a, b
