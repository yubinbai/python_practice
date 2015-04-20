import random


def quicksort(array):
    quicksortHelper(array, 0, len(array) - 1)


def quicksortHelper(array, p, r):
    if (p < r):
        q = partition(array, p, r)
        quicksortHelper(array, p, q - 1)
        quicksortHelper(array, q + 1, r)


def partition(array, p, r):
    key = array[r]
    i = p - 1
    for q in range(p, r):
        if (array[q] < key):
            i += 1
            swap(array, i, q)
    swap(array, i + 1, r)
    return i + 1


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


array = [random.randint(1, 100000) for x in range(1000)]
quicksort(array)
for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
        print('test failed')
