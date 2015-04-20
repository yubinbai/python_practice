"""
The Bellman-Ford algorithm

iter(graph) gives all nodes
iter(graph[u]) gives neighbours of u
graph[u][v] gives weight of edge (u, v)
"""


def bellman_ford(graph, source):
    def relax(u, v):
        d1 = d[u] + graph[u][v]
        if d[v] > d1:
            d[v] = d1
            pre[v] = u
    d = {}
    pre = {}
    for node in graph:
        d[node] = float('Inf')
        pre[node] = None
    d[source] = 0
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                relax(u, v)
    # check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]:
                raise 'negative-weight cycle'
    return d, pre


def test():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
    }

    d, p = bellman_ford(graph, 'a')

    assert d == {
        'a':  0,
        'b': -1,
        'c':  2,
        'd': -2,
        'e':  1
    }

    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
    }

if __name__ == '__main__':
    test()
