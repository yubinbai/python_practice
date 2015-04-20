def bSearch(A, x):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) >> 1
        if A[mid] > x:
            right = mid
        elif A[mid] < x:
            left = mid + 1
        else:
            return mid
    return -1


def bisect_left(A, x):
    '''
    return first pos of x
    '''
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) >> 1
        if A[mid] >= x:
            right = mid
        else:
            left = mid + 1
    return left


def bisect_right(A, x):
    '''
    return next pos of last x
    '''
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) >> 1
        if A[mid] > x:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    A = list(range(0, 10000, 2))
    print bSearch(A, 100)
    A = [50] * 5 + [100] * 5 + [200] * 5
    print A
    print bisect_left(A, 100)
    print bisect_right(A, 100)
    print bisect_right(A, 300)
