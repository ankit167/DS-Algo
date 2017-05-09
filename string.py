import math


#
# Returns the longest palindromic substring
# T(n)- O(n^2), S(n)- O(n^2)
#
def longest_palindromic_substring(s):
    n = len(s)
    table = [[False for j in range(n)] for i in range(n)]
    for i in range(n):
        table[i][i] = True
    maxlen, start, end = 1, 0, 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            start = i
            end = i+1
            maxlen = 2
    for k in range(3, n+1):
        for i in range(0, n-k+1):
            j = i+k-1
            if s[i] == s[j] and table[i+1][j-1]:
                table[i][j] = True
                if k > maxlen:
                    maxlen = k
                    start = i
                    end = j
    return s[start:end+1]


#
# Print all palindromic substrings in a given string.
# T(n)- O(n^2), S(n)- O(n^2)
#
# The code is related to longest_palindromic_substring()
#
def all_palindromic_substrings(s):
    n = len(s)
    table = [[False for j in range(n)] for i in range(n)]
    for i in range(n):
        table[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = True

    for k in range(3, n+1):
        for i in range(0, n-k+1):
            j = i+k-1
            if s[i] == s[j] and table[i+1][j-1]:
                table[i][j] = True

    for i in range(n):
        for j in range(i, n):
            if table[i][j]:
                print s[i:j+1]


#
# Computes prefix array for KMP
#
def prefixCompute(f, patt, m):
    i, j = 1, 0
    f[0] = 0
    while i < m:
        if patt[i] == patt[j]:
            f[i] = j+1
            i += 1
            j += 1
        elif j > 0:
            j = f[j-1]
        else:
            f[i] = 0
            i += 1


#
# Searches a pattern in a string using KMP algorithm.
# Compute prefix array -> Compare string and pattern
# T(n)- O(n), S(n)- O(m)
# n- length of string, m- length of pattern
#
def KMP(string, patt):
    m, n = len(patt), len(string)
    f = [0 for i in range(m)]
    prefixCompute(f, patt, m)
    i, j = 0, 0
    while i < n:
        if string[i] == patt[j]:
            if j == m-1:
                return i-j
            i += 1
            j += 1
        elif j > 0:
            j = f[j-1]
        else:
            i += 1
    return -1


#
# Reverse a string
#
def reverse(s, start, end):
    if start > end:
        return
    i, j = start, end
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1


#
# Reverse words of a string
# Input: the game is on
# Output: on is game the
#
# T(n)- O(n)
#
def reverseWords(s):
    i = 0
    s = list(s)
    while i < len(s):
        while i < len(s) and s[i] == ' ':
            i += 1
        start = i
        while i < len(s) and s[i] != ' ':
            end = i
            i += 1
        reverse(s, start, end)
    reverse(s, 0, len(s)-1)
    s = ''.join(x for x in s)
    print s


#
# Print the longest substring in a string, that does not contain any
# repeating characters.
#
# T(n)- O(n)
# S(n)- O(NO_OF_CHARS)
#
def longestSubstringWithoutDuplicates(str):
    NO_OF_CHARS = 256
    visited = [-1] * NO_OF_CHARS
    visited[ord(str[0])] = 0
    curlen, maxlen, start, end = 1, 1, 0, 0
    for i in range(1, len(str)):
        prev_index = visited[ord(str[i])]
        if prev_index == -1 or prev_index < i - curlen:
            curlen += 1
            end += 1
        else:
            if curlen > maxlen:
                maxlen = curlen
                st, en = start, end
            curlen = i - prev_index
            start, end = prev_index+1, i
        visited[ord(str[i])] = i
    print maxlen, st, en


#
# Input: aaabbccdee
# Output: a3b2c2d1e2
#
def replace_character_count(s):
    n = len(s)
    i = 0
    while i < n:
        p = i
        c = 1
        while i < n-1 and s[i] == s[i+1]:
            i += 1
            c += 1
        s = s[:p+1] + str(c) + s[i+1:]
        i = p + int(math.log(c, 10) + 1) + 1
        n = len(s)
    print s


def main():
    s = raw_input()
    all_palindromic_substrings(s)
    # replace_character_count(s)

if __name__ == "__main__":
    main()
