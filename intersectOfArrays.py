# Find the intersection of two sorted arrays.


def intersection(array1, array2):
    i = j = 0
    results = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            i += 1
        elif array2[j] < array1[i]:
            j += 1
        else:
            results.append(array1[i])
            i += 1
            j += 1
    return results

if __name__ == '__main__':
    array1 = range(0, 100, 2)
    array2 = range(0, 200, 5)

    print(intersection(array1, array2))
