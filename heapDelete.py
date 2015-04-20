import heapq


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):  # when zero is here, gives -1
    return (i - 1) // 2


def heapDelete(h, pos):
    p = parent(pos)  # move all top parents down a slot
    while p >= 0:
        h[pos] = h[p]
        pos = p
        p = parent(p)

    h[0] = h[len(h) - 1]  # put last one on top
    h.pop()  # remove last element
    heapify(h, 0)


def heapify(h, pos):
    if pos >= len(h):
        return

    l = left(pos)
    if l >= len(h):
        return

    r = right(pos)
    if r >= len(h):
        return

    smallest = pos
    if h[l] < h[pos]:
        smallest = l
    if h[r] < h[smallest]:
        smallest = r

    if smallest != pos:
        swap = h[smallest]
        h[smallest] = h[pos]
        h[pos] = swap

        heapify(h, smallest)

if __name__ == '__main__':
    import random
    data = [random.randint(1, 100) for x in range(10)]

    heapq.heapify(data)
    print(data)

    heapDelete(data, 2)
    print(data)
