

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

    # Taking care of the edge cases- matrix of size 1xn or mx1
    for i in range(n):
        count[0][i] = 1
    for j in range(m):
        count[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            # Number of ways to reach a[i][j] = number of ways to reach
            #                                   a[i-1][j] + a[i][j-1]
            count[i][j] = count[i-1][j] + count[i][j-1]

    return count[m-1][n-1]


#
# Rotate a n*n matrix clockwise by 90 degree (inplace)
# Approach: (a) Layer by Layer rotation (Discussed below)
#           (b) Find transpose of the matrix and reverse all rows
# T(n)- O(n^2)
#
# Note: To rotate anti-clockwise, find transpose and reverse all columns
#       To rotate a matrix by 180 degree (clockwise/anticlockwise),
#          (a) swap ith row with n-i-1th row
#          (b) reverse each row of the matrix
#
def rotateClockwise(a, n):
    for layer in range(0, n//2):
        first, last = layer, n-layer-1
        for i in range(first, last):
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


#
# Find transpose of a matrix.
# First row becomes first column and so on.
#
# T(n)- O(row*col)
#
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


#
# Utility function to recursively search for a word in a matrix.
#
def search_word_util(a, s, visited, i, j, k, m, n):
    visited[i][j] = True
    if k == len(s)-1:
        return True
    k += 1
    i1 = i-1

    while i1 <= i+1 and i1 < m:
        j1 = j-1
        while j1 <= j+1 and j1 < n:
            if i1 >= 0 and j1 >= 0 and a[i1][j1] == s[k] and not visited[i1][j1]:
                p = search_word_util(a, s, visited, i1, j1, k, m, n)
                if p:
                    return p
            j1 += 1
        i1 += 1

    visited[i][j] = False
    return False


#
# Given a matrix of characters. Check if a given word is present in the matrix.
# For a given cell, We are allowed to move in any of the 8 directions.
#
# Approach: DFS
#           T(n)- O(m*n)
#
# Variation:
# In case of multiple input words, use trie approach. Create a trie with the
# input words. Start from the root, Match current character with root and
# neighbouring characters with root's children, and traverse trie according.
# If we reach a leaf node of the trie successfully, it means we current processed
# string in present in the matrix.
# (Refer gfg)
#
def search_word(a, s):
    m, n = len(a), len(a[0])
    visited = [[False for j in range(n)] for i in range(m)]
    k = 0

    for i in range(m):
        for j in range(n):
            if a[i][j] == s[k] and not visited[i][j]:
                p = search_word_util(a, s, visited, i, j, k, m, n)
                if p:
                    return p
    return False


#
# Print a matrix in spiral order (clockwise)
# Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: 1 2 3 6 9 8 7 4 5
#
# T(n)- O(row*col)
#
# One liner solution:
# ```
# return arr & list(arr.pop(0)) + self.print_spiral(zip(*arr)[::-1])
# ```
# zip(*arr)[::-1]: creates transpose of a matrix, and reverses the order of rows
#
def print_spiral(arr):
    row_length, col_length = len(arr), len(arr[0])
    row_index, col_index = 0, 0
    i, j = 0, 0

    while row_index < row_length and col_index < col_length:
        for i in range(col_index, col_length):
            print arr[row_index][i],
        row_index += 1

        for i in range(row_index, row_length):
            print arr[i][col_length-1],
        col_length -= 1

        if row_index < row_length:
            for i in range(col_length-1, col_index-1, -1):
                print arr[row_length-1][i],
            row_length -= 1

        if col_index < col_length:
            for i in range(row_length-1, row_index-1, -1):
                print arr[i][col_index],
            col_index += 1


#
# Search a key in a row wise and column wise sorted matrix.
# T(n)- O(m+n)
#
def searchInaSortedMatrix(mat, m, n, key):
    i, j = m-1, 0
    while i >= 0 and j < n:
        if key == mat[i][j]:
            return True
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    return False


#
# Given a nxn matrix, return a saddle point in the matrix.
# A saddle point is an element which is minimum in its row and maximum
# in its column
#
# T(n)- O(n^2)
# Note: There can be more than one saddle points. Here, we are just
#       printing the first saddle point.
#
def saddle_point(mat, n):
    for i in range(n):
        min_row_element = mat[i][0]
        col_index = 0
        flag = 0

        # Finding the minimum element of the row
        for j in range(1, n):
            if mat[i][j] < min_row_element:
                min_row_element = mat[i][j]
                col_index = j

        # Check if the min_row_element, is the maximum element
        # in the corresponding column.
        for k in range(n):
            # If there is a single element in the column greater than
            # the min_row_element, break from the loop
            if min_row_element < mat[k][col_index]:
                flag = 1
                break

        if flag == 0:  # print the min_row_element if it is greatest in the column
            print min_row_element
            return True

    return False


def main():
    row, col = map(int, raw_input().split())
    a = []
    for i in range(row):
        l = list(map(int, raw_input().split()))
        a.append(l)
    saddle_point(a, row)

if __name__ == "__main__":
    main()
