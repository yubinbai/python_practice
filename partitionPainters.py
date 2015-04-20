'''
partition an array(N) of jobs to k painters, try to be even for painters
the wall being painted must be continuous
'''


def partitionPainters(data, painters):
    sumOfData = []
    currSum = 0
    for i in range(len(data)):
        currSum += data[i]
        sumOfData.append(currSum)  # sum from data[0] to data[i]
    return partitionPainterHelper(sumOfData, len(data), painters)


def partitionPainterHelper(sumOfData, n, k):
    if k == 1:
        return sumOfData[n - 1]
    minResult = sumOfData[-1]
    for j in range(k, n):
        currResult = max(partitionPainterHelper(
            sumOfData, j, k - 1), sumOfData[n - 1] - sumOfData[j - 1])
        if currResult < minResult:
            minResult = currResult
    return minResult


def partitionDP(data, k):
    n = len(data)
    sumOfData = []
    currSum = 0
    for i in range(len(data)):
        currSum += data[i]
        sumOfData.append(currSum)  # sum from data[0] to data[i]

    memo = [[0 for x in range(n + 1)] for y in range(k + 1)]
    for i in range(1, n + 1):
        memo[1][i] = sumOfData[i - 1]
    for j in range(2, k + 1):
        for i in range(j, n + 1):
            currMin = sumOfData[-1]
            for x in range(j, i):
                currResult = max(
                    memo[j - 1][x], sumOfData[i - 1] - sumOfData[x - 1])
                if currResult < currMin:
                    currMin = currResult
            memo[j][i] = currMin
    return memo[k][n]

if __name__ == '__main__':
    import random
    data = [random.randint(1, 100) for x in range(5)]

    painters = 3
    print(data)

    results = partitionPainters(data, painters)

    print(results)

    results = partitionDP(data, painters)

    print(results)
