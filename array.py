#!/usr/bin/python

import math
from collections import deque

#
# Find minimum element in each 'k' sized window. (Deque approach)
# T(n)- O(n), S(n)- O(n)
#
def findMinInWindow(a,k):
    n = len(a)
    l = deque()

    for i in range(k):
        while len(l) > 0 and a[i] <= a[l[-1]]:
            l.pop()
        l.append(i)

    for i in range(k,n):
        print a[l[0]]
        while len(l) > 0 and l[0] <= i-k:
            l.popleft()
        while len(l) > 0 and a[i] <= a[l[-1]]:
            l.pop()
        l.append(i)
    print a[l[0]]

#
# Given arrival and departure times of trains. Find minimum number of platforms required
# anytime, so that no arriving train is short of a platform.
# T(n)- O(nlogn)
#
def minPlatforms(arr, dep):
    result, platform, n = 1, 1, len(arr)
    arr.sort()
    dep.sort()
    i,j = 1,0
    while i < n and j < n:
        if arr[i] < dep[j]:
            platform += 1
            i += 1
            if platform > result:
                result = platform
        else:
            platform -= 1
            j += 1
    return result

#
# Search a key in a row wise and column wise sorted matrix.
# T(n)- O(m+n)
#
def searchInaSortedMatrix(mat, m, n, key):
    i,j = m-1, 0
    while i >=0 and j < n:
        if key == mat[i][j]:
            return True
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    return False

#
# A series of 0's is followed by 1's in an array. Find the start index of 1's.
# T(n)- O(logn).
# Hint: Use Binary Search, since the array is sorted.
#
def findStartOne(a,start,end):
    if start > end:
        return None
    mid = start + (end-start)/2
    if a[mid] == 1:
        if mid == start or a[mid-1] == 0:
            return mid
        return findStartOne(a,start,mid-1)
    else:
        return findStartOne(a,mid+1,end)

#
# Returns the maximum element in the array
#
def findMax(a):
    m = a[0]
    for i in a:
        if i > m:
            m = i
    return m

#
# In an array of positive integers (>= 1),
# find the minimum integer which is not present
# in the array. T(n)- O(n)
# Assume the elements are stored starting from index 1,
# Input: 6 4 1 5 12
# Output: 2
#
def minMissing(a):
    a.insert(0,0)
    m = findMax(a)
    d = len(str(m))
    y = int(math.pow(10,d))
    n = len(a)
    for i in range(1,n):
        x = a[i]% y
        if x >= n:
            continue
        a[x] += y
    for i in range(1,n):
        c = a[i]//y
        if c == 0:
            print i
            return

#
# Merge given intervals
# Input: [(1,3),(4,10),(20,25),(21,29),(2,5)]
# Output: (1,10), (20,29)
# Input list is a list of tuples, where for each tuple- t,
# t[0]- starting time, t[1]- ending time of interval
# Approach 1: Sort list in increasing order of start time. Use stack
#             T(n)- O(nlogn), S(n)- O(n)
# Approach 2: Sort list in non-increasing order of start time, and
#             maintain index. T(n)- O(nlogn) (Check gfg)
#
def mergeOverlappingIntervals(l):
    n = len(l)
    if n <= 0:
        return
    # Sorting list based on start time
    l.sort(key=lambda x: x[0])
    # Creating stack
    s = []
    s.append(l[0])
    for i in range(1, n):
        t = s[-1]
        # No overlap. current end time < Start time of the next element
        if t[1] < l[i][0]:
            s.append(l[i])
        # Overlap. current end time > next start time and < next end time
        elif t[1] < l[i][1]:
            # Creating a new tuple with updated values
            nt = (t[0],l[i][1])
            # Removing previous tuple and pushing the merged tuple
            s.pop()
            s.append(nt)

    while len(s) > 0:
        print s[-1],
        s.pop()

#
# Given an array of integers, find the largest subarray with 0 sum.
# Approach- Hashing. For each index i, keep a track of sum from 0th
#           to ith index- sum+= a[i]. If this sum has appeared before,
#           it means, we have a subarray of sum 0- Check length to keep
#           a track of maxlength. If it is not so, hash the sum with i.
# T(n)- O(n), S(n)- O(n)
#
def largestSubarrayWithZeroSum(a):
    s, maxlength, hmap = 0, 0, {}
    for i in range(len(a)):
        s += a[i]
        if a[i] == 0 and maxlength == 0:
            maxlength = 1
        # if is 0, then we have the largest current subarray
        # starting from index 0
        if s == 0:
            maxlength = i+1
        if not s in hmap:
            hmap[s] = i
        else:
            # s has appeared before. finding length and comparing
            # with maxlength
            l = i-hmap[s]
            maxlength = max(l, maxlength)
    return maxlength
# Exercise: We can also keep a track of start and end index of max subarray
#           and display them in the end.


def main():
    a = list(map(int, raw_input().split()))
    print largestSubarrayWithZeroSum(a)

if __name__=='__main__':
    main()

