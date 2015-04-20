from bitstring import BitArray
from math import sqrt
MAXN = 1000000


def prime_sieve(top=MAXN):
    b = BitArray(top)  # bitstring of ’0’ bits
    for i in range(2, top):
        if not b[i]:
            yield i
            # i is prime, so set all its multiples to ’1’.
        b.set(True, range(i * i, top, i))


def primefactors(n):
    '''
    lists prime factors of a natural number, from greatest to smallest
    '''
    result = []
    for p in primes:
        if p > sqrt(n):
            break
        while n % p == 0:
            result.append(p)
            n /= p
    if n != 1:
        result.append(n)
    return result

primes = list(prime_sieve(int(sqrt(MAXN) + 1)))

for i in range(MAXN):
    a = primefactors(i)
print a
