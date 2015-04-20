''' Insert into a Cyclic Sorted List Given a node from a cyclic linked list
which has been sorted, write a function to insert a value into the list such
that it remains a cyclic sorted list. The given node can be any single node in
the list. 
'''


class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data


def generateCyclic(size):
    head = Node(0)
    curr = head
    for i in range(1, size):
        n = Node(i)
        curr.next = n
        curr = n

    curr.next = head
    return head


def printCyc(head):
    curr = head.next
    result = [head.data]
    while curr != head:
        result.append(curr.data)
        curr = curr.next
    print(result)


def insert(cyc, data):
    prev = cyc
    curr = prev.next
    while curr != cyc:
        if (prev.data <= data and data < curr.data) or \
            (prev.data > curr.data and (data < curr.data or data > prev.data)):
            n = Node(data)
            prev.next = n
            n.next = curr
            return
        prev = curr
        curr = curr.next

    n = Node(data)
    prev.next = n
    n.next = curr


if __name__ == '__main__':
    c = generateCyclic(2)
    printCyc(c)

    curr = c
    for i in range(5):
        curr = curr.next

    insert(curr, -5)
    insert(curr, -1)
    printCyc(c)
