'''
generate all permutations of an iterable
'''


def permutation(array):
    def _permute(array, step):
        if step == len(array) - 1:
            results.append(list(array))
            return

        for i in range(step, len(array)):
            array[i], array[step] = array[step], array[i]
            _permute(array, step + 1)
            array[i], array[step] = array[step], array[i]

    results = []
    _permute(array, 0)
    return results


def uniquePermutations(array):
    def _uniquePermutations():
        if len(path) == len(array):
            results.append(list(path))
            return
        for i in range(len(array)):
            if used[i] or (i != 0 and array[i] == array[i - 1] and used[i - 1]):
                continue
            used[i] = True
            path.append(array[i])
            _uniquePermutations()
            used[i] = False
            path.pop()

    results = []
    used = [False for x in range(len(array))]
    path = []
    _uniquePermutations()
    return results


if __name__ == '__main__':
    data = list("abbd")
    # for row in permutation(data): print(''.join(row))
    for row in uniquePermutations(data):
        print(''.join(row))
