#!/usr/bin/python

import math, sys
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
    start, end = -1, -1
    for i in range(len(a)):
        s += a[i]
        if a[i] == 0 and maxlength == 0:
            maxlength = 1
            start, end = i, i
        # if s is 0, then we have the largest current subarray
        # starting from index 0
        if s == 0:
            maxlength = i+1
            start, end = 0, i
        if not s in hmap:
            hmap[s] = i
        else:
            # s has appeared before. finding length and comparing
            # with maxlength
            l = i-hmap[s]
            if l > maxlength:
                maxlength = l
                start, end = hmap[s]+1, i
    # printing length, start and end index of the max subarray
    print maxlength, start, end

#
# Find largest subarray with equal number of 0s and 1s
# Approach: Replace all 0s with -1. Call largestSubarrayWithZeroSum().
# T(n)- O(n), S(n)- O(n)
# Note: We are modifying the contents of the array here.
#
def largestSubarrayWithEqualZerosAndOnes(a):
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = -1
    largestSubarrayWithZeroSum(a)


#
# Find subarray in an array of integers, such that the sum of elements in the
# subarray is equal to a given sum.
# Approach: Hashing. Similar to technique used in largestSubarrayWithZeroSum()
# T(n)- O(n), S(n)- O(n)
#
def subarrayWithGivenSum(a,s):
    currsum, start, end, hmap = 0, -1, -1, {}
    for i in range(len(a)):
        currsum += a[i]
        if currsum == s:
            start, end = 0, i
            break
        elif currsum-s in hmap:
            start, end = hmap[currsum-s]+1, i
            break
        hmap[currsum] = i
    print start,end


#
# Approach: Kadane's Algorithm
# Note: if 'sumsofar' is initialized to 0, the algo won't work for the case
#       where all elements in the array are negative.
# T(n)- O(n)
#
def largestSumContiguousSubarray(a):
    sumsofar = -sys.maxint-1 # Case of all elements being negative gets handled
    maxendinghere = 0
    s = 0
    for i in range(len(a)):
        maxendinghere += a[i]
        if sumsofar < maxendinghere:
            sumsofar = maxendinghere
            start,end = s,i
        if maxendinghere < 0:
            maxendinghere = 0
            s = i+1
    # print sum, start and end index of the max contiguous sum subarray.
    print sumsofar, start, end

#
# Given an array of 0s and 1s. Find the 0s that can be flipped in order to
# create max number of consecutive 1s in the array. A maximum of 'm' 0s can
# be flipped.
# Input: 1 0 0 1 1 0 1 0 1 1 1, m = 2
# Output: 5 7 (Flip 0s at index 5 and 7)
# Output Array: 1 0 0 1 1 1 1 1 1 1 1
#
# Approach: Maintain a window and work. T(n)- O(n)
#
def zerosFlipped(a, m):
    wl, wr, n = 0, 0, len(a)
    bestl, bestwindow = 0, 0
    zerocount = 0

    while wr < n:

        if zerocount <= m:
            if a[wr] == 0:
                zerocount += 1
            wr += 1

        if zerocount > m:
            if a[wl] == 0:
                zerocount -= 1
            wl += 1

        if wr-wl > bestwindow:
            bestwindow = wr-wl
            bestl = wl

    for i in range(bestwindow):
        if a[bestl+i] == 0:
            print bestl+i,

#
# Given an array, where all numbers are repeated once,
# except two numbers. Find the two numbers.
# Input: 2 5 1 7 4 5 7 1
# Output: 2 4
# Approach: (i) Sort and compare adjacent numbers
#           (ii) xor operation (discussed below)
# T(n)- O(n)
#
#
def findTwoNonRepeatedNumbers(a):
    xor, x, y = 0, 0, 0
    for item in a:
        xor = xor ^ item
    # finds the rightmost set bit of xor. Idea is, out of
    # the two elements, one will have this bit set as 1
    # and the other will have this bit set as 0. Using this
    # info, we can group elements and find the two elements.
    rightsetbit = xor & ~(xor-1)
    for item in a:
        if item & rightsetbit:
            x = x ^ item
        else:
            y = y ^ item

    print x,y
    '''
    Note:
    This problem can be generalized. Given an array, where
    two elements have odd occurances, and all the other elements
    have even occurances. Find the two numbers. Same soln would work.
    '''

'''
Given an array, where every other element occurs 3 times and only one
element occurs once. Find the element.
Approach- We can sum the bits in the same positions for all the elements
          and take modulo with 3. The bits for which the sum is not a
          multiple of 3 are the bits of the number occuring once.
T(n)- O(n*INT_SIZE)
'''
def findSingleNonRepeatedNumber(a):
    n, result = len(a), 0
    for i in range(0,32):
        s = 0
        x = 1 << i
        for j in range(n):
            if a[j] & x:
                s += 1
        if s%3:
            result = result | x
    print result

def main():
    a = list(map(int, raw_input().split()))
    findSingleNonRepeating(a)

if __name__=='__main__':
    main()

