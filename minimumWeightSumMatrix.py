
# 
# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right, which minimizes 
# the sum of all numbers along its path.
#
#
# Note: You can only move either down or right at any point in time.

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    for diag in range(2, n+m): # start from the 2nd diagonal 
        startCol = max(0, diag - m)
        count = min(diag, m, n - startCol)

        for j in range(0,count):
            row = min(m, diag) - j - 1
            col = startCol + j
            
            a, b = -1,-1
            if row > 0:
                a = grid[row-1][col]
            if col > 0:
                b = grid[row][col - 1]


            if a == -1:
                grid[row][col] += b
            elif b == -1:
                grid[row][col] += a
            else:
                grid[row][col] += min(a,b)
    
    return grid[-1][-1]


def diagonalSearch(grid):
    m = len(grid)
    n = len(grid[0])

    for diag in range(1, n+m): # start from the 2nd diagonal 
        startCol = max(0, diag - m)
        count = min(diag, m, n - startCol)

        for j in range(0,count):
            row = min(m, diag) - j - 1
            col = startCol + j
            print(grid[row][col])
        

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
diagonalSearch(grid)

print('------------')

grid = [ [1,  2,  3,  4,  5,  6,  7,  8],
         [9, 10, 11, 12, 13, 14, 15, 16]]
diagonalSearch(grid)