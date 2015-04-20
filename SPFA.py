from numpypy import *
from collections import deque
from heapq import *
import random
import time
INF = 1 << 30
N = 200


def shortestPathFasterAlgorithm(source):
    d = zeros((N + 1))
    d.fill(INF)
    d[source] = 0
    q = deque()
    q.append(source)
    while q:
        v1 = q.popleft()
        for v2 in range(N + 1):
            if d[v1] + graph[v1, v2] < d[v2]:
                d[v2] = d[v1] + graph[v1, v2]
                if v2 not in q:
                    q.append(v2)
    return d


def dijkstra(source):
    dist = zeros((N + 1))
    for i in range(N + 1):
        dist[i] = graph[source, i]
    dist[source] = 0
    visited = zeros((N + 1), dtype=byte)
    heap = []
    for i in range(N + 1):
        heappush(heap, (dist[i], i))
    visitedCount = 0
    while visitedCount <= N:
        d1, v1 = heappop(heap)
        if visited[v1]:
            continue
        dist[v1] = d1
        visited[v1] = 1
        visitedCount += 1
        for v2 in range(N + 1):
            value = graph[v1, v2] + d1
            if dist[v2] > value:
                dist[v2] = value
                heappush(heap, (value, v2))
    return dist

# make graph
graph = zeros((N + 1, N + 1))
for i in range(N + 1):
    for j in range(i + 1, N + 1):
        graph[j, i] = graph[i, j] = random.random()


millis1 = int(round(time.time() * 1000))
for i in range(N + 1):
    shortestPathFasterAlgorithm(i)
    # shortestPathFasterAlgorithm(0)
millis2 = int(round(time.time() * 1000))
print("SPFA Time in milliseconds: %d " % (millis2 - millis1))
millis1 = int(round(time.time() * 1000))
for i in range(N + 1):
    dijkstra(i)
millis2 = int(round(time.time() * 1000))
print("Dijkstra Time in milliseconds: %d " % (millis2 - millis1))

'''
for i in range(N + 1):
    r1 = shortestPathFasterAlgorithm(i)
    r2 = dijkstra(i)
    for j in range(N + 1):
        if r1[j] != r2[j]:
            print 'error', r1[j], r2[j]
print 'No error.'
'''
