'''
Created on 2013-6-16

@author: Yubin Bai
'''
import unittest
import random
from longestIncreastingSequence import LIS, LIS2, LIS3


class Test(unittest.TestCase):

    def setUp(self):
        self.maxN = 100
        self.array = random.sample(range(self.maxN * 10), self.maxN)

    def tearDown(self):
        pass

    def testLCSLIS(self):
        L, A = LIS(self.array)
        for i in range(L - 1):
            self.assertTrue(A[i] <= A[i + 1])

    def testLCSLIS2(self):
        L, A = LIS2(self.array)
        for i in range(L - 1):
            self.assertTrue(A[i] <= A[i + 1])

    def testEq(self):
        L, A = LIS(self.array)
        L1, A1 = LIS2(self.array)
        self.assertEqual(L, L1)

    def testLCSLIS3(self):
        L, A = LIS3(self.array)
        L1, A1 = LIS2(self.array)
        self.assertEqual(L, L1)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testLCSLIS']
    unittest.main()
