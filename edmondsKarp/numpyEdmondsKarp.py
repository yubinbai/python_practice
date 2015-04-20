'''
Created on 2013-11-12

@author: Yubin Bai
'''
from collections import deque
from itertools import combinations
import numpy as np
INF = 1 << 32


def edmondsKarp(graph, n, s, t):

    def augmentPath(v, minEdge):
        if (v == s):  # managed to get back to source
            currFlow[0] = minEdge  # minEdge of the path
            return
        elif not p[v] is None:  # augment if there is a path
            # we need AdjMat for fast lookup here
            augmentPath(p[v], min(minEdge, graph[p[v], v]))
            graph[p[v], v] -= currFlow[0]  # forward edges -> decrease
            graph[v, p[v]] += currFlow[0]  # backward edges -> increase

    p = [None] * n  # parent map to reconstruct path
    currFlow = [0]  # global variables, use list as mutable

    maxFlow = 0
    while True:  # this will be run max O(VE) times
        currFlow[0] = 0
        q = deque()
        dist = [INF] * n
        dist[s] = 0  # O(E) BFS and record path p
        q.append(s)
        while q:
            u = q.popleft()  # queue: layer by layer!
            if (u == t):
                break  # modification 1: reach sink t, stop BFS
            for v in range(n):  # for each neighbors of u
                # modification 2: also check AdjMat as edges may disappear
                if graph[u, v] > 0 and dist[v] == INF:
                    dist[v] = dist[u] + 1  # then v is reachable from u
                    q.append(v)  # enqueue v for next steps
                    p[v] = u  # modification 3: parent of v->first is u

        augmentPath(t, INF)  # path augmentation in O(V)
        if (currFlow[0] == 0):
            break  # seems that we cannot pass any more flow
        maxFlow += currFlow[0]
    return maxFlow

if __name__ == '__main__':
    # combination of adj list and adj matrix
    n = 10
    graph = np.zeros((n, n), dtype=np.byte)
    d = {1: {3: 70, 4: 30}, 3: {2: 25, 4: 5},
         4: {2: 70}, 2: {}}
    for a in d:
        for b in d[a]:
            graph[a, b] = d[a][b]
    maxFlow = edmondsKarp(graph, n, 1, 2)
    print("Max flow = %d\n" % maxFlow)
