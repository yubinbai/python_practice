import random


class Vertex:
    neighbors = []
    prevIndex = 0

    def __init__(self, e):
        self.data = e


def generateGraph(size=10):
    vertices = []
    for i in range(size):
        node = Vertex(i)
        vertices.append(node)
        node.neighbors = [random.randint(0, 3) for x in range(size)]
    return vertices


def DFS(vertices, start):
    touched = set()
    fresh = set(vertices)

    result = []
    _DFSVisit(vertices, touched, fresh, start, result)
    while len(fresh) > 0:
        for v in vertices:
            if v in fresh:
                _DFSVisit(vertices, touched, fresh, v, result)

    return result


def _DFSVisit(vertices, touched, fresh, v, result):
    touched.add(v)
    fresh.remove(v)

    neighbors = []
    for i in range(len(v.neighbors)):
        if v.neighbors[i] != 0:
            neighbors.append(vertices[i])

    for u in neighbors:
        if u in fresh:
            u.prevIndex = v.data
            _DFSVisit(vertices, touched, fresh, u, result)

    touched.remove(v)
    result.append(v)

if __name__ == '__main__':
    v = generateGraph(20)
    result = DFS(v, v[0])
    resultAndPrev = [(v.data, v.prevIndex) for v in result]
    print(resultAndPrev)
