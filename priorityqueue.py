# use priority queue to implement stack and queue

import heapq


class stack:
    data = []
    highestPriority = 0
    lowestPriority = 0

    def push(self, e):
        self.highestPriority -= 1  # smaller value means priority is higher
        heapq.heappush(self.data, (self.highestPriority, e))

    def pop(self):
        if not s.isEmpty():
            self.highestPriority += 1
            return heapq.heappop(self.data)[1]
        else:
            return None

    def isEmpty(self):
        return self.highestPriority >= self.lowestPriority


class queue:
    data = []
    highestPriority = 0
    lowestPriority = 0

    def enqueue(self, e):
        self.lowestPriority += 1  # increase the lowest priority (lowering)
        heapq.heappush(self.data, (self.lowestPriority, e))

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            # increaste the highest priority (lowering it )
            self.highestPriority += 1
            return heapq.heappop(self.data)[1]

    def isEmpty(self):
        if self.highestPriority >= self.lowestPriority:
            self.highestPriority = 0
            self.lowestPriority = 0
            return True
        else:
            return False


def heapsort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h, i)

    return [heapq.heappop(h) for x in range(len(iterable))]

if __name__ == '__main__':
    import random
    data = [random.randint(1, 100) for x in range(15)]
    data.sort()
    '''
	s = stack()
	for i in data:
		s.push(i)

	while not s.isEmpty():
		print(s.pop())
	'''
    q = queue()
    for i in data:
        q.enqueue(i)

    while not q.isEmpty():
        print(q.dequeue())
