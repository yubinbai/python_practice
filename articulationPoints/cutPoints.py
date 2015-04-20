'''
Created on Jun 22, 2013
@author: Yubin Bai
All rights reserved.
'''


def getSeparation(graph):
    def dfs(u):
        dfsLowpoint[u] = dfsNumber[u] = dfsNumberCounter[0]
        dfsNumberCounter[0] += 1
        for v in graph[u]:
            if (dfsNumber[v] == 0):  # a tree edge
                dfsParent[v] = u
                if (u == dfsRoot):  # special case
                    rootChildren[0] += 1  # count children of root
                dfs(v)
                if (dfsLowpoint[v] >= dfsNumber[u]):
                    cutPoints[u] = True
                if (dfsLowpoint[v] > dfsNumber[u]):  # for bridge
                    bridges.append((u, v))
                dfsLowpoint[u] = min(dfsLowpoint[u], dfsLowpoint[v])
            elif (v != dfsParent[u]):  # a back edge and not direct cycle
                dfsLowpoint[u] = min(dfsLowpoint[u], dfsNumber[v])
    dfsLowpoint = {}
    dfsNumber = {}
    dfsParent = {}
    cutPoints = {}
    dfsNumberCounter = [1]
    for v in graph:
        cutPoints[v] = False
        dfsNumber[v] = 0
        dfsParent[v] = None
    bridges = []
    for k in graph:
        if dfsNumber[k] == 0:
            dfsRoot = k
            rootChildren = [0]
            dfs(k)
            # special case
            cutPoints[dfsRoot] = (rootChildren[0] > 1)
    cutPts = [k for k in cutPoints if cutPoints[k]]
    return bridges, cutPts


if __name__ == '__main__':
    graph = {0: [1, -1], 1: [0, 2, 3, 4, 5], 2: [1], 3:
             [1], 4: [1, 5], 5: [1, 4], -1: [-2, 0], -2: [-1]}

    bridges, cutPoints = getSeparation(graph)
    print bridges, cutPoints
