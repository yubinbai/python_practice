# edid distance problem (word ladder)


def distance(source, target):
    n = len(source)
    m = len(target)
    memo = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(m + 1):
        memo[0][i] = i

    for i in range(n + 1):
        memo[i][0] = i

    for length in range(2, m + n + 1):
        for i in range(1, length):
            j = length - i
            if i - 1 < n and j - 1 < m:
                if source[i - 1] == target[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = min(memo[i - 1][j] + 1, memo[i][j - 1] + 1)

    return memo[n - 1][m - 1]

if __name__ == '__main__':
    s = 'abacdef'
    t = 'abcddefef'
    print(distance(s, t))
