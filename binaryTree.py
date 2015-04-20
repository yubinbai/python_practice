import random


class Node:
    data = None
    leftChild = None
    rightChild = None

    def __init__(self, data=None):
        self.data = data


def generateBST(data):
    def _generateBST(data, start, end):
        if start <= end:
            mid = int((start + end) / 2)
            root = Node(data[mid])
            root.leftChild = _generateBST(data, start, mid - 1)
            root.rightChild = _generateBST(data, mid + 1, end)
            return root
        else:
            return None
    length = len(data)
    return _generateBST(data, 0, length - 1)


def iterativeInOrder(root, result):
    stack = []
    current = root
    while len(stack) > 0 or current != None:
        if current != None:
            stack.append(current)
            current = current.leftChild
        else:
            current = stack.pop()
            result.append(current.data)
            current = current.rightChild


def inOrder(root, result):
    if root != None:
        inOrder(root.leftChild, result)
        result.append(root.data)
        inOrder(root.rightChild, result)


def maxDepth(root):
    if root == None:
        return 0
    else:
        depth1 = maxDepth(root.leftChild)
        depth2 = maxDepth(root.rightChild)
        return 1 + max(depth1, depth2)

if __name__ == '__main__':
    data = sorted([random.randint(1, 1000) for x in range(100)])
    bst = generateBST(data)

    result = []
    inOrder(bst, result)
    print(result)

    result = []
    iterativeInOrder(bst, result)
    print(result)

    print(maxDepth(bst))
