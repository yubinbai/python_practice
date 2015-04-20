import operator

a = reduce(operator.xor, range(10))
b = reduce(operator.xor, range(0, 5) + range(6, 10))
print a, b, a ^ b
