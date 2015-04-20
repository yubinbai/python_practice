def isPrime(n):
    for x in range(2, int(n / 2) + 1):
        if n % x == 0:
            return False
    return True


prime = []
for n in range(2, 100):
    if (isPrime(n)):
        prime.append(n)

print(prime)
