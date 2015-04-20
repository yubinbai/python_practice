'''
Created on 2013-6-25

@author: Yubin Bai
'''
import numpy as np

if __name__ == '__main__':
    mat = np.arange(1, 21).reshape(4, 5)
    print(mat)
    n, m = 4, 5
    
    for i in range(n):
        for j in range(m):
            print mat[i, j + (m - 1 - 2 * j) * (i % 2)],
        print
        
    for d in range(1, m + n):
        if d <= n:
            i, j = d - 1, 0
        else:
            i, j = n - 1, d - n
        while i in range(n) and j in range(m):
            print mat[i, j],
            i -= 1
            j += 1
        print
