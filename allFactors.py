import math
import unittest
import time
import collections

def allFactors(number):
    result = []
    for i in range(1, int(math.sqrt(number)) + 1):
        a, b = divmod(number, i)
        if b == 0:
            if i < a:
                result.append(i)
                result.append(a)
            else:
                if a == i:
                    result.append(a)
                break
    result.sort()
    return result


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


def getAllFactors(primeFactors):
    def backtrack(step):
        if step == N:
            aFactor = 1
            for j, p in enumerate(path):
                aFactor *= factors[j] ** p
            result.add(aFactor)
            return
        for i in range(counter[factors[step]] + 1):
            path[step] = i
            backtrack(step + 1)
            path[step] = 0

    counter = collections.Counter(primeFactors)
    factors = counter.keys()
    factors.sort()
    N = len(factors)
    path = [0] * N

    result = set()
    backtrack(0)
    result = list(result)
    result.sort()
    return result


class factorsTestCase(unittest.TestCase):

    def setUp(self):
        self.number = 1200000000000

    def test_prime(self):
        millis1 = int(round(time.time() * 1000))
        factors = primeFactors(self.number)
        f1 = getAllFactors(factors)
        millis2 = int(round(time.time() * 1000))
        print("Use prime factors product in milliseconds: %d " %
              (millis2 - millis1))

    def test_iterative(self):
        millis1 = int(round(time.time() * 1000))
        f2 = allFactors(self.number)
        millis2 = int(round(time.time() * 1000))
        print("Brute force Time Time in milliseconds: %d " %
              (millis2 - millis1))

if __name__ == '__main__':
    unittest.main()
