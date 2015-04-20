'''
Created on 2013-6-16

@author: Yubin Bai
'''
from memoized import memoized


def LIS(array):
    array1 = sorted(array)
    return LCS(array, array1)


def LIS2(array):
    array1 = sorted(array)
    return LCS_list(array, array1)


def longestIncreasing(array):
    """
    return N (length), path(list) as a tuple describing the subsequence

    O(n log n)

    memo[j] stores the position k of the
    smallest value X[k] such that there is an increasing subsequence of length j
    ending at X[k] on the range k <= i
    prev[k] stores the position of the predecessor of X[k] in the longest increasing
    subsequence ending at X[k].

    """

    memo = [0]
    prev = [0] * len(array)
    prev[0] = -1
    for i in range(1, len(array)):
        # if next one is greater, add into the sequence
        if array[memo[-1]] < array[i]:
            prev[i] = memo[-1]
            memo.append(i)
            continue
        # binary search for the best update point
        low = 0
        high = len(memo) - 1
        while low < high:
            mid = (low + high) // 2
            if array[memo[mid]] < array[i]:
                low = mid + 1
            else:
                high = mid
        # update if the new value is smaller
        if array[i] < array[memo[low]]:
            if low > 0:
                prev[i] = memo[low - 1]
            memo[low] = i

    path = []
    p = memo[-1]
    N = len(memo)
    for i in range(N):
        path.append(array[p])
        p = prev[p]
    path.reverse()
    return N, path


def LCS(a1, a2):
    @memoized
    def _lcs(p1, p2):
        if p1 == -1 or p2 == -1:
            return 0, -1
        if a1[p1] == a2[p2]:
            l1, x = _lcs(p1 - 1, p2 - 1)
            return l1 + 1, 0
        l1, x = _lcs(p1 - 1, p2)
        l2, x = _lcs(p1, p2 - 1)
        if l1 > l2:
            return l1, 1
        else:
            return l2, 2

    M = len(a1)
    N = len(a2)
    for i in range(M):
        for j in range(N):
            _lcs(i, j)

    i = M - 1
    j = N - 1
    result = []
    while i > -1 and j > -1:
        m, p = _lcs(i, j)
        if p == 0:
            result.append(a1[i])
            i -= 1
            j -= 1
        elif p == 1:
            i -= 1
        elif p == 2:
            j -= 1
        else:
            break
    result.reverse()
    return len(result), result


def LCS_list(a1, a2):
    M = len(a1)
    N = len(a2)
    memo = []
    for i in range(M + 1):
        row = [None] * (N + 1)
        memo.append(row)

    for i in range(M + 1):
        memo[i][0] = 0, -1

    for j in range(N + 1):
        memo[0][j] = 0, -1

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if a1[i - 1] == a2[j - 1]:
                l1, p1 = memo[i - 1][j - 1]
                memo[i][j] = l1 + 1, 0
            else:
                l1, p1 = memo[i - 1][j]
                l2, p2 = memo[i][j - 1]
                if l1 > l2:
                    memo[i][j] = l1, 1
                else:
                    memo[i][j] = l2, 2

    i = M
    j = N
    result = []
    while i > 0 and j > 0:
        l1, p = memo[i][j]
        if p == 0:
            result.append(a1[i - 1])
            i -= 1
            j -= 1
        elif p == 1:
            i -= 1
        elif p == 2:
            j -= 1
    result.reverse()
    return len(result), result

if __name__ == '__main__':
    a, b = longestIncreasing([81, 67, 42, 63, 5, 24, 7, 72, 29, 86])
    print(a)
    print(b)
