class Node:
    left = None
    right = None

    def __init__(self, data):
        self.data = data


def triangleTransverse(root, result):
    result.append(root)
    visitLeft(root.left, True, result)
    visitRight(root.right, True, result)


def visitLeft(root, visit, result):
    if root == None:
        return
    if visit or (root.left == None and root.right == None):
        result.append(root)
    visitLeft(root.left, True, result)
    visitLeft(root.right, False, result)


def visitRight(root, visit, result):
    if root == None:
        return
    visitRight(root.left, False, result)
    visitRight(root.right, True, result)
    if visit or (root.left == None and root.right == None):
        result.append(root)


def generateBST(data, rootPos):
    if rootPos >= len(data):
        return None
    root = Node(data[rootPos])
    root.left = generateBST(data, 2 * rootPos + 1)
    root.right = generateBST(data, 2 * rootPos + 2)
    return root

if __name__ == '__main__':

    data = [x for x in range(15)]
    root = generateBST(data, 0)
    print(data)
    result = []
    triangleTransverse(root, result)
    print([x.data for x in result])
