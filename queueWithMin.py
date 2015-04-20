''' Design a queue that supports push_rear, pop_front, and get_min in O(1).
Would that be elegantly possible too? '''

import collections


class minQueue:
    data = collections.deque()
    minCandidates = collections.deque()  # save the possible mins

    def isEmpty(self):
        return len(self.data) == 0

    def dequeue(self):
        if self.isEmpty():
            return None
        if self.minCandidates[0] == self.data[0]:
            self.minCandidates.popleft()
        return self.data.popleft()

    def enqueue(self, e):
        self.data.append(e)

        while len(self.minCandidates) > 0 and self.minCandidates[0] >= e:
            self.minCandidates.popleft()

        self.minCandidates.append(e)

    def min(self):
        if self.isEmpty():
            return None
        return self.minCandidates[0]

if __name__ == '__main__':
    import random
    data = [random.randint(1, 100) for x in range(15)]

    print(data)

    q = minQueue()
    for i in data:
        q.enqueue(i)
        print(q.min())

    print

    for i in data:
        q.dequeue()
        print(q.min())
