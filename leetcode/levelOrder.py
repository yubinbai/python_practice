import collections


class Node:
    leftChild = None
    rightChild = None

    def __init__(self, data=None):
        self.data = data


def levelTransversal(root):
    currLevel = collections.deque()
    nextLevel = collections.deque()
    result = []
    currLevel.append(root)
    while len(currLevel) > 0:
        x = currLevel.popleft()
        result.append(x.data)
        if x.leftChild != None:
            nextLevel.append(x.leftChild)
        if x.rightChild != None:
            nextLevel.append(x.rightChild)
        if len(currLevel) == 0:
            print(result)
            result = []
            swap = currLevel
            currLevel = nextLevel
            nextLevel = swap


def getLevel(level, root, result):
    if level == 1 and root != None:
        result.append(root.data)
    elif root != None:
        getLevel(level - 1, root.leftChild, result)
        getLevel(level - 1, root.rightChild, result)


def iterativeLevelOrder(root):
    depth = maxDepth(root)
    for i in range(1, depth + 1):
        result = []
        getLevel(i, root, result)
        print(result)


def maxDepth(root):
    if root == None:
        return 0
    else:
        depth1 = maxDepth(root.leftChild)
        depth2 = maxDepth(root.rightChild)
        return 1 + max(depth1, depth2)


def inOrder(root, result):
    if root != None:
        inOrder(root.leftChild, result)
        result.append(root.data)
        inOrder(root.rightChild, result)


def generateTreeFromArray(data):
    return generateTreeHelper(data, 0, len(data))


def generateTreeHelper(data, root, max):
    if root < max:
        r = Node(data[root])
        r.leftChild = generateTreeHelper(data, 2 * root + 1, max)
        r.rightChild = generateTreeHelper(data, 2 * root + 2, max)
        return r
    else:
        return None

if __name__ == '__main__':
    data = [x for x in range(12)]
    tree = generateTreeFromArray(data)

    levelTransversal(tree)

    iterativeLevelOrder(tree)
