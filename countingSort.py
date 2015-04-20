import time
import random


def countingSort2(data, smallest, largest):
    counters = [0 for x in range(smallest, largest + 1)]
    for i in data:
        counters[i - smallest] += 1
    del data[:]
    for i, c in enumerate(counters):
        data.extend([smallest + i] * c)


def countingSort(data, smallest, largest):
    counters = [0 for x in range(smallest, largest + 1)]
    for i in data:
        counters[i - smallest] += 1
    dataPointer = len(data) - 1
    for i in range(len(counters) - 1, -1, -1):
        while counters[i] > 0:
            data[dataPointer] = i + smallest
            counters[i] -= 1
            dataPointer -= 1

if __name__ == '__main__':
    data = [random.randint(1, 10) for x in range(10000000)]
    data1 = list(data)

    millis1 = int(round(time.time() * 1000))
    countingSort(data, 1, 10)
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    countingSort2(data1, 1, 10)
    millis3 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis3 - millis2))
