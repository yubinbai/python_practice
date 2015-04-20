'''
Given a binary tree, print the elements in post-order iteratively without using recursion.
'''
import random


class Node:
    data = None
    leftChild = None
    rightChild = None

    def __init__(self, data=None):
        self.data = data


def generateBST(data):
    length = len(data)
    return generateBSTHelper(data, 0, length - 1)


def generateBSTHelper(data, start, end):
    if start <= end:
        mid = int((start + end) / 2)
        root = Node(data[mid])
        root.leftChild = generateBSTHelper(data, start, mid - 1)
        root.rightChild = generateBSTHelper(data, mid + 1, end)
        return root
    else:
        return None


def preOrderInversed(tree, result):
    if tree == None:
        return
    result.append(tree.data)
    if tree.rightChild != None:
        preOrderInversed(tree.rightChild, result)
    if tree.leftChild != None:
        preOrderInversed(tree.leftChild, result)


def postOrder(tree, result):
    if tree == None:
        return
    if tree.leftChild != None:
        postOrder(tree.leftChild, result)
    if tree.rightChild != None:
        postOrder(tree.rightChild, result)
    result.append(tree.data)


def iterativePostOrder(root, result):
    current = root
    stack = []

    while len(stack) > 0 or current != None:
        if current != None:
            if current.leftChild != None and current.leftChild not in result:
                stack.append(current)
                current = current.leftChild
            elif current.rightChild != None and current.rightChild not in result:
                stack.append(current)
                current = current.rightChild
            else:
                result.append(current)
                current = None
        else:
            current = stack.pop()


if __name__ == '__main__':
    data = sorted([random.randint(1, 1000) for x in range(6)])
    bst = generateBST(data)

    result = []
    preOrderInversed(bst, result)
    print(result[::-1])

    result = []
    postOrder(bst, result)
    print(result)

    result = []
    iterativePostOrder(bst, result)
    result = [x.data for x in result]
    print(result)
