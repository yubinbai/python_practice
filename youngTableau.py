import random
import sys

maxSize = 100


class Young:
    data = [[0 for i in range(maxSize)] for j in range(maxSize)]
    size = 0

    # rearrange the tableau
    def _youngify(self, i, j):
        largestI = i
        largestJ = j
        if i - 1 >= 0 and self.data[i][j] < self.data[i - 1][j]:
            largestI = i - 1
            largestJ = j
        if j - 1 >= 0 and self.data[largestI][largestJ] < self.data[i][j - 1]:
            largestI = i
            largestJ = j - 1
        if largestJ != j or largestI != i:
            self._swap(largestI, largestJ, i, j)
            self._youngify(largestI, largestJ)

    def insertElement(self, e):
        self.size += 1
        if self.size == maxSize ** 2:
            raise 'Full table'
        i = maxSize - 1
        j = maxSize - 1
        self.data[i][j] = e
        self._youngify(i, j)

    def _swap(self, i1, j1, i2, j2):
        s = self.data[i1][j1]
        self.data[i1][j1] = self.data[i2][j2]
        self.data[i2][j2] = s

    def verify(self):
        for i in range(maxSize - 1):
            for j in range(maxSize - 1):
                if self.data[i][j] > self.data[i + 1][j] or self.data[i][j] > self.data[i][j + 1]:
                    return False
        return True

if __name__ == '__main__':
    # generate an array of random numbers
    data = [random.randint(1, 1000) for x in range(5000)]

    y = Young()
    for i in data:
        try:
            y.insertElement(i)
        except:
            print 'Table is Full'
            break

    print('Is valid?', y.verify())
