'''
Created on Jun 22, 2013

@author: Yubin Bai

All rights reserved.
'''


def edgeTypes(graph):
    DFS_GRAY, DFS_BLACK, DFS_WHITE = 1, 2, 0
    dfs_num = {}
    dfs_parent = {}
    for v in graph:
        dfs_num[v] = DFS_WHITE

    def graphCheck(u):  # DFS for checking graph edge properties...
        dfs_num[u] = DFS_GRAY  # color this as GRAY (temporary)
        for v in graph[u]:  # traverse this AdjList
            if dfs_num[v] == DFS_WHITE:  # GRAY to WHITE
                print("Tree Edge (%d, %d)" % (u, v))
                dfs_parent[v] = u  # parent of this children is me
                graphCheck(v)
            elif dfs_num[v] == DFS_GRAY:  # GRAY to GRAY
                if (v == dfs_parent[u]):
                    print("Bidirectional (%d, %d) - (%d, %d)" % (u, v, v, u))
                else:
                    print("Back Edge (%d, %d) (Cycle)" % (u, v))
            elif dfs_num[v] == DFS_BLACK:  # GRAY to BLACK
                print("Forward/Cross Edge (%d, %d)" % (u, v))
        dfs_num[u] = DFS_BLACK  # now color this as BLACK (DONE)

    for i in range(len(graph)):
        if dfs_num[i] == DFS_WHITE:
            graphCheck(i)

if __name__ == '__main__':
    graph = {0: [1], 1: [2, 3], 2: [1, 3], 3:
             [1, 2, 4], 4: [3], 5: [], 6: [7], 7: [6]}

    edgeTypes(graph)
