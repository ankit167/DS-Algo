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
# Find the longest palindromic subsequence in a given string
# Input: "BBABCBCAB"
# Output: 7 ("BABCBAB")
#
# T(n)- O(n^2), S(n)- O(n^2)
#
# Exercise: Print the desired longest palindromic subsequence
# (https://stackoverflow.com/questions/12892912/
#  how-to-find-the-longest-palindromic-subsequence-not-its-length)
#
def longest_palindromic_subsequence(s):
    n = len(s)
    l = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        l[i][i] = 1

    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j] and k == 2:
                l[i][j] = 2
            elif s[i] == s[j]:
                l[i][j] = l[i+1][j-1] + 2
            else:
                l[i][j] = max(l[i+1][j], l[i][j-1])

    return l[0][n-1]


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
#
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
def reverse_words(s):
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
def longest_substring_without_duplicates(str):
    NO_OF_CHARS = 256
    # stores last visited index of a character
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


#
# Given a list of strings. Group all the anagrams together.
# The order of the group of anagrams may not be important.
#
# Input: ["eat", "ant", "tea", "bat", "nat", "tan"]
# Output: [["ant", "nat", "tan"], ["bat"], ["eat", "tea"]]
#
# T(n)- O(nmlogm) (n- length of the list. m- length of each string)
# S(n)- O(n)
#
# Also refer to:
# http://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
#
def group_anagrams(strs):
    d = {}
    for s in strs:
        # Sort each string and map the original string to the
        # sorted string
        p = ''.join(sorted(s))
        if p not in d:
            d[p] = [s]
        else:
            d[p].append(s)
    return [d[k] for k in d]


#
# Given a string, find the first non-repeating character in the string
# Input: "abaacbdadea"
# Output: c
#
# Approaches: (i) Scan the string and maintain the count of each character.
#                 Again, scan the array and keep track of the min index, such
#                 that the count is 1. Return the character at the min index.
#                 T(n)- O(n), S(n)- O(n)
#                 Drawback: Requires two scans of the entire string.
#
#            (ii) Instead of count, keep track of the occurance index. The
#                 next scan would be on the auxilliary array (of length 26)
#                 rather than the entire string. (Discussed below)
#                 T(n)- O(n), S(n)- O(n)
#                 Drawback: Still requires multiple scans
#
#           (iii) Maintain a doubly linked list along with auxilliary array.
#                 The array would store the addresses of the elements in the
#                 DLL. Update the array and the DLL in such a way that, at the
#                 end of the string scan, the head of the DLL returns the output
#                 ( O(1) time to fetch the output )
#                 T(n)- O(n), S(n)- O(n)
#
def first_non_repeating_character(s):
    #
    # Values at occ[i]
    # -1: The character is not present in the string at all
    # -2: The character has occurred multiple times
    # > -1: The index of the first occurance of the character.
    #
    occ = [-1]*26  # Assuming the string contains only alphabets
    n = len(s)

    for i in range(n):
        ch = s[i]
        index = ord(ch)-97
        if occ[index] == -1:
            occ[index] = i
        elif occ[index] > -1:
            occ[index] = -2

    min_index = n
    for i in range(26):
        # Finding the min index for the first occurance of a character
        if occ[i] >= 0 and occ[i] < min_index:
            min_index = occ[i]

    if min_index < n:  # There is atleast one character that occurs only once
        return s[min_index]


def main():
    s = raw_input()
    print first_non_repeating_character(s)

if __name__ == "__main__":
    main()
