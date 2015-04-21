if __name__ == '__main__':
    mat = []
    mat.append(range(1, 6))
    mat.append(range(7, 12))
    mat.append(range(13, 18))
    mat.append(range(19, 24))
    print(mat)
    n, m = 4, 5
   
    # snake order 
    for i in range(n):
        for j in range(m):
            print mat[i][j + (m - 1 - 2 * j) * (i % 2)],
        print
        
    # diagonal order
    for d in range(1, m + n):
        if d <= n:
            i, j = d - 1, 0
        else:
            i, j = n - 1, d - n
        while i in range(n) and j in range(m):
            print mat[i][j],
            i -= 1
            j += 1
        print
