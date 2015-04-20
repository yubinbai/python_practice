import random
import heapq
# use min heap to merge k sorted list


def mergeK(arrays, merged):
    k = len(arrays)
    pointers = [0 for x in range(k)]
    heap = []
    for x in range(k):
        heapq.heappush(heap, (arrays[x][pointers[x]], x))

    while len(heap) > 0:
        number, x = heapq.heappop(heap)
        merged.append(number)
        if pointers[x] + 1 < len(arrays[x]):
            pointers[x] += 1
            heapq.heappush(heap, (arrays[x][pointers[x]], x))

if __name__ == '__main__':
    arrays = []
    for x in range(3):
        arrays.append([])
        arrays[x] = [random.randint(1, 100)
                     for i in range(random.randint(4, 10))]
        arrays[x].sort()
    print(arrays)

    merged = []
    mergeK(arrays, merged)
    print(merged)
