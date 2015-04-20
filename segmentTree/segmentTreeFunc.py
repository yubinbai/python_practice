'''
Created on Jun 18, 2013

@author: Yubin Bai

Segment Tree Library
The segment tree is stored like a heap array
'''
import unittest


class SegmentTreeFunc:

    def __init__(self, N, func):
        self.length = 1
        while self.length < 2 * N:
            self.length <<= 1
        self.tree = [0] * self.length
        self.func = func

    def buildTree(self, A):
        self._buildTree(A, 1, 0, len(A) - 1)

    def _buildTree(self, A, node, b, e):
        if b == e:
            self.tree[node] = b
        else:
            left = 2 * node
            right = 2 * node + 1
            self._buildTree(A, left, b, (b + e) // 2)
            self._buildTree(A, right, (b + e) // 2 + 1, e)
            i1, i2 = self.tree[left], self.tree[right]
            if self.func(A[i1], A[i2]) == A[i1]:
                self.tree[node] = i1
            else:
                self.tree[node] = i2

    def query(self, A, i, j):
        def _query(A, node, b, e, i, j):
            if i > e or j < b:
                return -1
            if b >= i and e <= j:
                return self.tree[node]
            p1 = _query(A, 2 * node, b, (b + e) // 2, i, j)
            p2 = _query(A, 2 * node + 1, (b + e) // 2 + 1, e, i, j)
            if p1 == -1:
                return p2
            if p2 == -1:
                return p1
            if self.func(A[p1], A[p2]) == A[p1]:
                return p1
            else:
                return p2
        return _query(A, 1, 0, len(A) - 1, i, j)

    def update(self, A, pos, value):
        '''
        update A[pos] to a new value
        '''
        if self.func(A[pos], value) == A[pos]:
            raise KeyError
        A[pos] = value

        def _update(node, p, b, e):
            if p < b or p > e:
                return
            if b == e:
                self.tree[node] = p
                return
            if self.func(A[p], A[self.tree[node]]) == A[p]:
                self.tree[node] = p
            _update(node * 2, p, b, (b + e) // 2)
            _update(node * 2 + 1, p, (b + e) // 2 + 1, e)
        _update(1, pos, 0, len(A) - 1)

    def updateRange(self, A, i, j, value):
        '''
        update the values in range [i, j] of A to be new value
        '''
        def _update(node, b, e):
            if i > e or j < b:
                return
            if b == e:
                self.tree[node] = b
                A[b] = value
                return
            i1 = self._query(A, node, b, e, i, j)
            if self.func(A[i1], value) == A[i1]:
                return
            _update(node * 2, b, (b + e) // 2)
            _update(node * 2 + 1, (b + e) // 2 + 1, e)
            self.tree[node] = i1
        _update(1, 0, len(A) - 1)


class Test(unittest.TestCase):

    def testMax(self):
        A = [8, 7, 3, 9, 5, 1, 10]
        t = SegmentTreeFunc(len(A), max)
        t.buildTree(A)
        self.assertEqual(3, t.query(A, 1, 3))
        t.update(A, 2, 19)
        self.assertEqual(2, t.query(A, 1, 3))
        t.update(A, 2, 33)
        self.assertEqual(2, t.query(A, 1, 3))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()
