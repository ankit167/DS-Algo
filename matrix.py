
#
# Count the number of unique paths from a[0][0] to a[m-1][n-1]
# We are allowed to move either right or down from a cell in the matrix.
# Approaches-
# (i) Recursion- Recurse starting from a[m-1][n-1], upwards and leftwards,
#                add the path count of both recursions and return count.
# (ii) Dynamic Programming- Start from a[0][0].Store the count in a count
#                           matrix. Return count[m-1][n-1]
# T(n)- O(mn), S(n)- O(mn)
#
def countPaths(m, n):
    if m < 1 or n < 1:
        return -1
    count = [[None for j in range(n)] for i in range(m)]

    #Taking care of the edge cases- matrix of size 1xn or mx1
    for i in range(n):
        count[0][i] = 1
    for j in range(m):
        count[j][0] = 1

    for i in range(1,m):
        for j in range(1,n):
            # Number of ways to reach a[i][j] = number of ways to reach
            #                                   a[i-1][j] + a[i][j-1]
            count[i][j] = count[i-1][j] + count[i][j-1]

    return count[m-1][n-1]

'''
Rotate a n*n matrix clockwise by 90 degree (inplace)
Approach: (a) Layer by Layer rotation (Discussed below)
          (b) Find transpose of the matrix and reverse all rows
T(n)- O(n^2)

Note: To rotate anti-clockwise, find transpose and reverse all columns
      To rotate a matrix by 180 degree (clockwise/anticlockwise),
          (a) swap ith row with n-i-1th row
          (b) reverse each row of the matrix
'''
def rotateClockwise(a, n):
    for layer in range(0,n//2):
        first,last = layer, n-layer-1
        for i in range(first,last):
            offset = i-first
            top = a[first][i]
            # rotate left to top
            a[first][i] = a[last-offset][first]
            # rotate bottom to left
            a[last-offset][first] = a[last][last-offset]
            # rotate right to bottom
            a[last][last-offset] = a[i][last]
            # rotate top to right
            a[i][last] = top
    return a

'''
Find transpose of a matrix.
First row becomes first column and so on.

T(n)- O(row*col)
'''
def transpose(a, row, col):
    for i in range(row):
        for j in range(i, col):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp
    return a

# Print a matrix
def display(a, row, col):
    for i in range(row):
        for j in range(col):
            print a[i][j],
        print

def main():
    row,col = map(int, raw_input().split())
    a = []
    for i in range(row):
        l = list(map(int, raw_input().split()))
        a.append(l)
    a = transpose(a,row,col)
    display(a,row,col)

if __name__ == "__main__":
    main()
