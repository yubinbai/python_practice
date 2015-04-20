import operator
import time

millis1 = int(round(time.time() * 1000))
x = reduce(operator.mul, range(1, 100000))
millis2 = int(round(time.time() * 1000))
print("Time in milliseconds: %d " % (millis2 - millis1))
