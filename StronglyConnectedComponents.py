'''
Created on Jun 22, 2013

@author: Yubin Bai

All rights reserved.
'''


def stronglyConnectedComponents(graph):
    DFS_WHITE = 0
    dfsNum = {}  # number of a node
    dfsLowNum = {}  # lowest number met before this node
    dfsNumCounter = [0]
    dfsSCC = []
    inStack = set()
    for v in graph:
        dfsNum[v] = DFS_WHITE
    resultStr = []

    def tarjanSCC(u):
        dfsNumCounter[0] += 1
        dfsLowNum[u] = dfsNum[u] = dfsNumCounter[0]
        dfsSCC.append(u)
        inStack.add(u)  # stores u based on order of visitation
        for v in graph[u]:
            if dfsNum[v] == DFS_WHITE:  # a tree edge
                tarjanSCC(v)
            if v in inStack:  # condition for update
                dfsLowNum[u] = min(
                    dfsLowNum[u], dfsLowNum[v])  # update dfsLowNum[u]

        # after dfs for the branch
        if dfsLowNum[u] == dfsNum[u]:  # if this is a root of SCC
            resultStr.append("SCC: ")
            while (dfsSCC and dfsSCC[-1] != u):
                v = dfsSCC[-1]
                resultStr.append("%d " % v)
                inStack.remove(v)
                dfsSCC.pop()

            v = dfsSCC[-1]
            resultStr.append("%d\n" % v)
            inStack.remove(v)
            dfsSCC.pop()

    for v in graph:
        if dfsNum[v] == DFS_WHITE:
            tarjanSCC(v)
    print(''.join(resultStr))


if __name__ == '__main__':
    graph = {0: [1], 1: [3], 2: [1], 3: [2, 4], 4: [5], 5: [7], 6: [4], 7: [6]}

    stronglyConnectedComponents(graph)
