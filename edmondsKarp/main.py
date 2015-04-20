'''
Created on 2013-6-24

@author: Yubin Bai
'''
from collections import deque
from itertools import combinations
INF = 1 << 32


def edmondsKarp(graph, s, t):

    def augmentPath(v, minEdge):
        if (v == s):  # managed to get back to source
            currFlow[0] = minEdge  # minEdge of the path
            return
        elif (v in p):  # augment if there is a path
            # we need AdjMat for fast lookup here
            augmentPath(p[v], min(minEdge, graph[p[v]][v]))
            graph[p[v]][v] -= currFlow[0]  # forward edges -> decrease
            graph[v][p[v]] += currFlow[0]  # backward edges -> increase

    p = {}  # parent map to reconstruct path
    currFlow = [0]  # global variables, use list as mutable

    maxFlow = 0
    while True:  # this will be run max O(VE) times
        currFlow[0] = 0
        q = deque()
        dist = {s: 0}  # O(E) BFS and record path p
        q.append(s)
        while q:
            u = q.popleft()  # queue: layer by layer!
            if (u == t):
                break  # modification 1: reach sink t, stop BFS
            for v in graph[u]:  # for each neighbors of u
                # modification 2: also check AdjMat as edges may disappear
                if graph[u][v] > 0 and v not in dist:
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
    graph = {1: {3: 70, 4: 30}, 3: {2: 25, 4: 5},
             4: {2: 70}, 2: {}}
    for v1, v2 in combinations(graph, 2):
        if v1 in graph[v2] and v2 not in graph[v1]:
            graph[v1][v2] = 0
        if v2 in graph[v1] and v1 not in graph[v2]:
            graph[v2][v1] = 0
    maxFlow = edmondsKarp(graph, 1, 2)
    print("Max flow = %d\n" % maxFlow)
    # it does change the original graph
    print graph
