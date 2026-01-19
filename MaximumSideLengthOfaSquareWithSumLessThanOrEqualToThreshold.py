
def maxSideLength(mat, threshold):
    m, n = len(mat), len(mat[0])

    # Instead of an n×m matrix, create an (n+1)×(m+1) matrix.
    # This way, we don’t have to worry about index handling when creating the prefix array.
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    # Notice how useful the previous trick was
    for i in range(m):
        for j in range(n):
            prefix[i + 1][j + 1] = (
                prefix[i][j + 1]
                + prefix[i + 1][j]
                - prefix[i][j]
                + mat[i][j]
            )

    left, right = 1, min(m, n)
    ans = 0

    # Perform binary search directly on the diagonal length.
    # This trick is not mine, but it is so ingenious that not crediting it would be a shame.
    while left <= right:
        mid = (left + right) // 2
        isValid = False

        for i in range(mid, m + 1):
            for j in range(mid, n + 1):
                total = (
                    prefix[i][j]
                    - prefix[i - mid][j]
                    - prefix[i][j - mid]
                    + prefix[i - mid][j - mid]
                )
                if total <= threshold:
                    isValid = True
                    break
            if isValid:
                break
        
        if isValid:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans
    

# Ex1 
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]] 
threshold = 4
res = maxSideLength(mat, threshold)
print(res)


# Ex2 
mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
threshold = 1
res = maxSideLength(mat, threshold)
print(res)