import random


class Node:
    data = left = right = None

    def __init__(self, data=None):
        self.data = data


def generateTreeFromArray(data):
    return generateTreeHelper(data, 0, len(data))


def generateTreeHelper(data, root, right):
    if root < right:
        r = Node(data[root])
        r.left = generateTreeHelper(data, 2 * root + 1, right)
        r.right = generateTreeHelper(data, 2 * root + 2, right)
        return r
    else:
        return None


def findNode(root, x):
    if root == None:
        return None
    if root.data == x:
        return root
    left = findNode(root.left, x)
    if left != None:
        return left
    right = findNode(root.right, x)
    if right != None:
        return right


def LCA(root, p, q):
    if root == None:
        return None
    if root == p or root == q:
        return root
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left != None and right != None:
        return root

    if left != None:
        return left
    else:
        return right


if __name__ == '__main__':
    size = 15
    data = [x for x in range(size)]
    root = generateTreeFromArray(data)

    p = random.randint(1, size - 1)
    q = random.randint(1, size - 1)

    n1 = findNode(root, p)
    n2 = findNode(root, q)

    n3 = LCA(root, n1, n2)

    for i in [n1, n2, n3]:
        print(i.data)
