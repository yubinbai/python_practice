from heapq import *
import numpy as np
import random
import time
INF = 1 << 30
N = 300


def dijkstra(source):
    dist = np.zeros(N)
    for i in range(N):
        dist[i] = edgeWeight[source, i]
    dist[source] = 0
    visited = np.zeros(N, dtype=np.byte)
    queue = []
    for i in range(N):
        heappush(queue, (dist[i], i))
    visitedCount = 0
    while visitedCount <= N and queue:
        d1, v1 = heappop(queue)
        if visited[v1]:
            continue
        dist[v1] = d1
        visited[v1] = 1
        visitedCount += 1
        for v2 in range(N):
            shorterD = edgeWeight[v1, v2] + d1
            if dist[v2] > shorterD:
                dist[v2] = shorterD
                heappush(queue, (shorterD, v2))
    return dist


edgeWeight = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        edgeWeight[i, j] = random.random()


millis1 = int(round(time.time() * 1000))
for i in range(N):
    dijkstra(i)
millis2 = int(round(time.time() * 1000))
print("Time in milliseconds: %d " % (millis2 - millis1))
