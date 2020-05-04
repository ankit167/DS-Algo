#!/usr/bin/python

import math
import sys
from collections import deque


#
# Find minimum element in each 'k' sized window. (Deque approach)
# T(n)- O(n), S(n)- O(n)
#
# Other approaches- Create a BST of size 'k'. In each iteration, print the
#                   min node value. Delete the i-kth node. Insert the next value.
#                   T(n)- O(nlogk). Same can be done by creating a heap of
#                   size 'k'.
#
def findMinInWindow(a, k):
    n = len(a)
    l = deque()

    if n == 0 or k <= 0:
        return

    for i in range(k):
        while len(l) > 0 and a[i] <= a[l[-1]]:
            l.pop()
        l.append(i)

    for i in range(k, n):
        print a[l[0]]
        while len(l) > 0 and l[0] <= i-k:
            l.popleft()
        while len(l) > 0 and a[i] <= a[l[-1]]:
            l.pop()
        l.append(i)
    print a[l[0]]


#
# Given arrival and departure times of trains. Find minimum number of
# platforms required anytime, so that no arriving train is short of a platform.
# T(n)- O(nlogn)
#
# The same question can be asked in a different way. Given the start and end time
# of a set of meetings. Find the minimum number of meeting rooms needed.
#
# Companies: Google, Facebook, Snapchat
#
def minPlatforms(arr, dep):
    result, platform, n = 1, 1, len(arr)
    arr.sort()
    dep.sort()
    i, j = 1, 0
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
# A series of 0's is followed by 1's in an array. Find the start index of 1's.
# T(n)- O(logn).
# Hint: Use Binary Search, since the array is sorted.
#
def findStartOne(a, start, end):
    if start > end:
        return None
    mid = start + (end-start)/2
    if a[mid] == 1:
        if mid == start or a[mid-1] == 0:
            return mid
        return findStartOne(a, start, mid-1)
    else:
        return findStartOne(a, mid+1, end)


#
# In an array of positive integers (>= 1),
# find the minimum postive integer which is not present
# in the array. T(n)- O(n)
# Assume the elements are stored starting from index 1
# Input: 6 4 1 5 12
# Output: 2
#
# Exercise: Solve the same problem, where the array contains
#           both positive and negative integers
# Link:     https://leetcode.com/problems/first-missing-positive
# Solution: https://pastebin.com/TqUCn65i
#
def minMissing(a):
    a.insert(0, 0)
    m = max(a)
    d = len(str(m))
    y = int(math.pow(10, d))
    n = len(a)
    for i in range(1, n):
        x = a[i] % y
        if x >= n:
            continue
        a[x] += y
    for i in range(1, n):
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
# Approach  : Sort list in increasing order of start time. Use stack
#             T(n)- O(nlogn), S(n)- O(n)
#
def merge_overlapping_intervals(l):
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
            nt = (t[0], l[i][1])
            # Removing previous tuple and pushing the merged tuple
            s.pop()
            s.append(nt)

    while len(s) > 0:
        print s[-1],
        s.pop()


#
# Merge given intervals
# Input: [(1,3),(4,10),(20,25),(21,29),(2,5)]
# Output: (1,10), (20,29)
#
# Approach  : Sort list in increasing order of start time. Keep
#             merging current index with previous index, as long as
#             there is an overlap, and then move to next index.
#             T(n)- O(nlogn)
#
def merge_overlapping_intervals_optimized(l):
    l.sort(key=lambda x: x[0])
    i, n = 1, len(l)

    while i < n:
        # if start time of current interval is greater then end time of
        # previous interval, it means there is no overlap.
        if l[i][0] > l[i-1][1]:
            i += 1
            continue
        # Overlap. Current interval is either partially or completely
        # overlapping with previous interval.
        # In case of partial overlap, create a new merged interval, update the
        # previous interval with the merged interval, delete the current
        # interval.
        # In case of complete overlap (current interval is complete subset
        # of previous interval), simply delete the current interval
        if l[i][1] > l[i-1][1]:
            nt = (l[i-1][0], l[i][1])
            l[i-1] = nt
        del l[i]  # delete current interval and decrement length of the list
        n -= 1

    return l


#
# Given a set of intervals, and a range. Find the intervals within the range,
# that are not present in the set of intervals
# Input: [(4,10),(3,8),(12,20)]
#        Range: 0-25
# Output: [(0,3),(10,12),(20,25)]
#
# Approach: Merge the given intervals. Iterate over the merged intervals, to
#           print the missing intervals between the range.
#
# T(n)- O(nlogn) S(n)- O(n)
#
# XXX We should run more test cases to verify the code.
#
def find_missing_intervals(l, start, end):
    l = merge_overlapping_intervals_optimized(l)
    lt = []

    if start < l[0][0]:  # Edge cases
        if end <= l[0][0]:
            print [(start, end)]
            return
        lt.append((start, l[0][0]))

    i = 1
    while i < len(l):
        prev_end = l[i-1][1]
        next_start = l[i][0]

        if end > next_start:
            if start <= prev_end:
                lt.append((prev_end, next_start))
            elif start > prev_end and start < next_start:
                lt.append((start, next_start))

        elif end >= prev_end and end <= next_start:
            if start <= prev_end:
                lt.append((prev_end, end))
            elif start >= prev_end:
                lt.append((start, end))
        i += 1

    if end > l[-1][1]:  # Edge cases
        if start > l[-1][1]:
            lt.append((start, end))
        else:
            lt.append((l[-1][1], end))

    print lt


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
        if s not in hmap:
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
# If the constraint is not to modify the array, then in
# largestSubarrayWithZeroSum(), modify s += a[i] to:
#     s = s+1 if a[i] == 1 else s-1
# The rest of the algorithm remains as is, and code should work correctly.
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
def subarrayWithGivenSum(a, s):
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
    print start, end


#
# Find the number of subarrays with a given sum.
# Input: [1,1,4,2,3,1,2,4]  k = 6
# Output: 5
#
def num_of_subarrays_with_given_sum(nums, k):
    d = {}
    currsum, res, n = 0, 0, len(nums)

    for i in range(n):
        currsum += nums[i]
        if currsum == k:
            res += 1
        if currsum-k in d:
            res += d[currsum-k]
        if currsum in d:
            d[currsum] = d[currsum] + 1
        else:
            d[currsum] = 1
    return res


#
# Given an array of integers, find the subarray with largest sum.
#
# Approach: Kadane's Algorithm
# Note: if 'sumsofar' is initialized to 0, the algo won't work for the case
#       where all elements in the array are negative.
#
# T(n)- O(n)
#
def largestSumContiguousSubarray(a):
    sumsofar = -sys.maxint-1  # Case of all elements being negative handled
    maxendinghere = 0
    s = 0
    for i in range(len(a)):
        maxendinghere += a[i]
        if sumsofar < maxendinghere:
            sumsofar = maxendinghere
            start, end = s, i
        if maxendinghere < 0:
            maxendinghere = 0
            s = i+1
    # print sum, start and end index of the max contiguous sum subarray.
    return (sumsofar, start, end)


#
# Find largest sum of elements in an array, such that no two elements
# are adjacent.
#
# Approach- Use two variables- incl (include an element),
#                              excl (exclude an element) and work along
#
# Note: This question can also be asked for a circular array. 
#       In a circular array, the last element and the
#       first element are considered adjacent. In that case,
#       we need to call this method twice, for a[0:n-1] and a[1:n], and
#       return the max result from these two calls.
#
# Companies- Directi
#
# T(n)- O(n)
#
def largestSumNonAdjacent(a):
    '''
    incln- include current element
    excln- exclude current elemment
    inclp- previous element is included
    exclp- previous element is excluded
    s- sum of elements
    '''
    n, s = len(a), 0
    inclp, exclp = a[0], 0
    for i in range(1, n):
        incln = exclp + a[i]
        excln = inclp
        s = max(incln, excln)
        inclp = incln
        exclp = max(excln, exclp)
    print s


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

    print x, y
    '''
    Note:
    This problem can be generalized. Given an array, where
    two elements have odd occurances, and all the other elements
    have even occurances. Find the two numbers. Same soln would work.
    '''


#
# Given an array, where every other element occurs 3 times and only one
# element occurs once. Find the element.
# Approach- We can sum the bits in the same positions for all the elements
#           and take modulo with 3. The bits for which the sum is not a
#           multiple of 3 are the bits of the number occuring once.
# T(n)- O(n*INT_SIZE)
#
def findSingleNonRepeatedNumber(a):
    n, result = len(a), 0
    for i in range(0, 32):
        s = 0
        x = 1 << i
        for j in range(n):
            if a[j] & x:
                s += 1
        if s % 3:
            result = result | x
    print result


#
# Find the longest increasing subsequence of an array
# Approach- Dynamic Programming
#
# T(n)- O(n^2)
#
def lis(a):
    n = len(a)
    l = [1]*n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
    print max(l)


#
# In a sorted array, for a given key, find the index of the
# next greater element.
#
def ceil_index(a, l, r, key):
    while r - l > 1:
        m = l + (r-l)/2
        if a[m] >= key:
            r = m
        else:
            l = m

    return r


#
# Optimized code for longest increasing subsequence of an array
# T(n)- O(nlogn)
#
# Approach- http://www.geeksforgeeks.org/
#           longest-monotonically-increasing-subsequence-size-n-log-n/
#
def lis_optimized(a):
    n = len(a)
    tail_table = [-1 for x in range(n)]
    tail_table[0] = a[0]
    l = 1

    for i in range(1, n):
        if a[i] < tail_table[0]:
            # new smallest value
            tail_table[0] = a[i]

        elif a[i] > tail_table[l-1]:
            tail_table[l] = a[i]
            l += 1

        else:
            tail_table[ceil_index(tail_table, -1, l-1, a[i])] = a[i]

    print l


#
# Given two sorted arrays. We need to merge the arrays in such a way that,
# after complete sorting, the initial elements are present in the first
# array, and the remaining elements are present in the second array.
#
# Input: a1 = [1, 5, 9, 10, 15, 20]
#        a2 = [2, 3, 8, 13]
#
# Output: a1 = [1, 2, 3, 5, 8, 9]
#         a2 = [10, 13, 15, 20]
#
# Approach: Start with the last element of the second array iterating
#           backwards. For each element a2i, iterate first array backwards,
#           until an element a1j is found, such that a1j > a2i. Swap a1j and
#           a2i. Use insertion sort approach on a1 to find the correct
#           position of a1j.
#           T(n)- O(m*n) (m and n are the length of a1 and a2)
#
def merge_without_extra_space(a1, a2):
    m, n = len(a1), len(a2)
    for i in range(n-1, -1, -1):
        j = m-1
        while j >= 0 and a1[j] <= a2[i]:
            j -= 1
        if j >= 0:
            a1[j], a2[i] = a2[i], a1[j]
            temp = a1[j]
            # Insertion sort approach
            while j >= 1 and a1[j-1] > temp:
                a1[j] = a1[j-1]
                j -= 1
            a1[j] = temp
    print '%s\n%s' % (a1, a2)


#
# Given a digit sequence, count the number of possible decodings of the
# digit sequence.
#
# Input- digits = "121"
# Output- 3 (Possible decodings- ABA, AU, LA)
#
# Approach: Dynamic Programming
#           T(n)- O(n), S(n)- O(n)
#
# Companies: Grab
#
def count_decodings(s):
    n = len(s)
    count = [0 for x in range(n+1)]
    count[0], count[1] = 1, 1

    for i in range(2, n+1):
        if s[i-1] > '0':
            count[i] = count[i-1]
        if s[i-2] < '2' or (s[i-2] == '2' and s[i-1] < '7'):
            count[i] += count[i-2]

    print count[n]


#
# Find all triplets in a array having sum equal to 0
# Approach: Sorting and traversing the array from left and right
# T(n)- O(n^2)
#
# Exercise- Find all the pythagorean triplets in an array (a^2 + b^2 = c^2)
#           (i) Square all elements in the array
#           (ii) Sort the array
#           (iii) Traverse the array from left and right to check if triplets
#                 exist, based on the above condition.
#           T(n)- O(n^2)
#
def triplets_sum_zero(a):
    n = len(a)
    a.sort()

    for i in range(n):
        j, k = i+1, n-1
        while j < k:
            s = a[i] + a[j] + a[k]
            if s == 0:
                print a[i], a[j], a[k]
                j += 1
                k -= 1
            elif s < 0:
                j += 1
            else:
                k -= 1


#
# Given an array of positive integers
# Find the maximum sum subsequence of the array, such that the subsequence
# contains alternate even and odd integers.
# Input: 4 6 7 3 2 9
# Output: 24 [6, 7, 2, 9]
#
# TO DO: Display the subsequence as well.
#
def max_sum_subsequence_alt(a):
    max_even, max_odd, n = 0, 0, len(a)
    for i in range(n):
        if a[i] % 2 == 0:
            max_even = max(max_even, max_odd+a[i])
        else:
            max_odd = max(max_odd, max_even+a[i])
    print max(max_even, max_odd)


#
# Given 'n' non-negative integers denoting height of
# blocks having width '1'. Compute the amount water, that
# can be trapped after raining.
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]              _
# Output: 6                             _      | |_   _
#                                   _  | |_   _| | |_| |_
# T(n)- O(n), S(n)- O(n)          _| |_| | |_| | | | | | |
# Exercise- Compute in O(n) time, without using extra space.
#
def trap_rain_water(height):
    n = len(height)
    if n == 0:
        return 0

    left, right, w = [-1]*n, [-1]*n, 0

    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i-1], height[i])

    right[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], height[i])

    for i in range(n):
        w += min(left[i], right[i]) - height[i]

    return w


#
# Search an element in a sorted array (increasing)
#
# T(n)- O(log n)
#
def binary_search(arr, start, end, key):
    if start > end:
        return -1
    mid = start + (end-start)/2
    if arr[mid] == key:
        return mid
    if key < arr[mid]:
        return binary_search(arr, start, mid-1, key)
    return binary_search(arr, mid+1, end, key)


#
# Search an element in a sorted and rotated array.
# Approach: First, find the pivot element, such that the subarrays on both
#           side of the pivot are sorted. Then search for the key in the sorted
#           subarrays using binary search. If there is no such pivot, it would
#           mean that the array is sorted but not rotated. In this case, we
#           perform binary search over the entire array.
#
# T(n)- O(log n)
#
# Note: This approach requires more than one pass of binary search to find an
#       element. Refer to optimized solution that finds and element in a single
#       pass of binary search.
#
def search_in_sorted_rotated_array(arr, key):
    n = len(arr)
    pivot = find_pivot(arr, 0, n-1)
    print pivot

    # If we do not get a valid pivot, it means that the array is not
    # rotated at all
    if pivot == -1:
        return binary_search(arr, 0, n-1, key)

    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot-1, key)
    return binary_search(arr, pivot+1, n-1, key)


#
# Find the pivot element in a sorted and rotated array, such that the
# subarrays on both sides pivot element are sorted.
#
# Input: [3, 4, 5, 1, 2], Pivot: 1
#
# T(n)- O(log n)
#
def find_pivot(arr, start, end):
    if start > end:
        return -1
    if start == end:
        return start
    mid = start + (end-start)/2
    if mid > start and arr[mid-1] > arr[mid]:
        return mid
    if mid < end and arr[mid+1] < arr[mid]:
        return mid + 1
    if arr[start] >= arr[mid]:
        return find_pivot(arr, start, mid-1)
    return find_pivot(arr, mid+1, end)


#
# Optimized solution to find an element in a sorted and rotated array.
# Requires only one pass of binary search
#
# T(n)- O(log n)
#
def search_in_sorted_rotated_array_optimized(arr, start, end, key):
    if start > end:
        return -1

    mid = start + (end-start)/2
    if arr[mid] == key:
        return mid

    if arr[start] <= arr[mid]:
        if key >= arr[start] and key <= arr[mid]:
            return search_in_sorted_rotated_array_optimized(arr,
                                                            start, mid-1, key)
        return search_in_sorted_rotated_array_optimized(arr, mid+1, end, key)

    if key >= arr[mid] and key <= arr[end]:
        return search_in_sorted_rotated_array_optimized(arr, mid+1, end, key)
    return search_in_sorted_rotated_array_optimized(arr, start, mid-1, key)


#
# Given an array of 'n' elements. Update all the elements of the array to
# some minimum element 'x' (belonging to the array), such that the product 
# of all elements in the new array is strictly greater than the product of all 
# elements in the original array.
#
# Input: [4, 2, 1 10, 6]
# Output: 4 (4*4*4*4*4 > 4*2*1*10*6)
#
# Approach: Sort the array and use binary search approach
# T(n)- O(nlogn)
#
# Note: For larger numbers in the array, we need to make sure that the value
#       of the product of numbers does not overflow.
#
def min_value_for_greater_product(a):
    a.sort()
    n = len(a)
    pro, ans = 1, 0
    for num in a:
        pro = pro*num
    left, right = 0, n-1

    while left <= right:
        mid = left + (right-left)/2
        if int(pow(a[mid], n)) > pro:
            ans = a[mid]
            right = mid-1
        else:
            left = mid+1

    return ans


#
# Given an array of 0s and 1s. Rearrange all the 0s to the left side, and all
# the 1s to the right side of the array
#
# T(n)- O(n)
#
def segregate(a):
    n = len(a)
    x, y = 0, n-1

    while x < y:
        if a[x] == 1 and a[y] == 0:
            a[x], a[y] = a[y], a[x]
        elif a[x] == 0 and a[y] == 0:
            x += 1
        elif a[x] == 1 and a[y] == 1:
            y -= 1
        else:
            x += 1
            y -= 1
    return a


#
# Given an unsorted array of integers, sort the array into a wave like array.
# An array a[0..n-1] is sorted in wave form if
# a[0] >= a[1] <= a[2] >= a[3] <= a[4] >= ....
#
# Input: [3, 6, 5, 10, 7, 20]
# Output: [5, 3, 7, 6, 20, 10] (One of the possible solutions)
#
# Approach: (i) Sort the array, and swap adjacent elements
#               Input: [3, 6, 5, 10, 7, 20]
#               Sorted: [3, 5, 6, 7, 10, 20]
#               Output: [5, 3, 7, 6, 20, 10]
#               T(n)- o(nlogn)
#
#          (ii) We just need to make sure that all even indexed elements are
#               greater than their adjacent odd indexed elements. Traverse all
#               the even indexed elements and do the following:
#               (a) If current element is smaller than previous odd indexed
#                   element, swap the previous and the current element.
#               (b) If current element is smaller than next odd indexed
#                   element, swap the current and the next element.
#               T(n)- O(n) [Discussed below]
#
def wave_form(a):
    n = len(a)

    for i in range(0, n, 2):  # Traversing even indexed elements
        if i > 0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
        if i < n-1 and a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

    print a


#
# Given a set of integers, the task is to divide it into two sets S1 and S2
# such that the absolute difference between their sums is minimum.
#
# Input: [1, 6, 11, 5]
# Output: 1
# Explanation: subset1- [1, 6, 5], sum1- 12
#              subset2- [11], sum2- 11
#
# Approaches: Recursion. Generate all possible sums from all the values of
#             the array, and check which solution is most optimal.
#             T(n)- O(2^n)
#
#             Dynamic Programming. T(n)- O(n*k), k- sum of all elements in array
#
# http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#
def partition_for_min_difference(a):
    n, s = len(a), sum(a)  # sum of all elements in the array
    dp = [[False for j in range(s+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, s+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]  # If ith element is excluded
            if j-a[i-1] >= 0:  # If ith element is included
                dp[i][j] = dp[i][j] | dp[i-1][j-a[i-1]]

    diff = sys.maxint-1  # Initialize difference of the two sums
    for j in range(s/2, -1, -1):
        if dp[n][j] is True:
            diff = s-2*j
            break

    print diff


#
# Find maximum j-i, such that a[j] > a[i]
#
def max_difference_indexes(a):
    n = len(a)
    lmin = [None for i in range(n)]
    rmax = [None for i in range(n)]

    lmin[0] = a[0]
    for i in range(1, n):
        lmin[i] = min(lmin[i-1], a[i])

    rmax[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        rmax[i] = max(rmax[i+1], a[i])

    # Traverse both arrays from left to right for optimum j-i
    i, j, max_diff = 0, 0, -1
    while i < n and j < n:
        if lmin[i] < rmax[j]:
            max_diff = max(max_diff, j-i)
            j += 1
        else:
            i += 1

    return max_diff

#
# For each element, print the first element to the right,
# which is greater than the current element. If there is no
# such element, print -1
#
# Input: [4, 1, 5, 7, 3, 8, 2]
# Output: [5, 5, 7, 8, 8, -1, -1]
#
# Approach: For each element, we are popping the previous processed
#           elements from the stack and deciding on whether the current
#           element is the next greater element for a popped element
# T(n)- O(n)
# S(n)- O(n)
#
# Note: The worst case occurs when the numbers are sorted in
#       decreasing order.
#
def next_greater_element(a):
    i, n = 1, len(a)

    st, res = [], [-1]*n
    st.append(0)

    while (i < n):
        while (len(st) > 0 and a[i] > a[st[-1]]):
            res[st.pop()] = a[i]
        st.append(i)
        i += 1

    return res


#
# Given an array consisting of 0s, 1s and 2s. Arrange them in such a way that
# all 0s are followed by 1s, followed by 2s.
#
# Input: [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
#
# T(n)- O(n)
#
def dutch_national_flag(a):
    n = len(a)
    low, mid, high = 0, 0, n-1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a


#
# Given an array of consecutive integers [1,2 ... n], where we are allowed
# to swap any two elements. Find the minimum number of swaps required to make
# the array sorted in ascending order
#
# Input: [2, 3, 4, 1, 5]
# Output: 3
#
# T(n) = O(n)
#
def minimumSwaps(arr):
    i, c, n = 0, 0, len(arr)
    while i < n:
        if arr[i] == i+1:
            i += 1
            continue
        b = arr[i] - 1
        if b > 0 and b < n:
            arr[i], arr[b] = arr[b], arr[i]
            c += 1
        else:
            i += 1
    return c


#
# Given an array represented as a number, where each
# element of the array is a digit. Add 1 to the number.
#
# Input: [9, 9, 9]
# Output: [1, 0, 0, 0]
#
# T(n)- O(n)
#
def plus_one(digits):
    carry = 1
    for i in range(len(digits)-1,-1,-1):
        s = digits[i] + carry
        digits[i] = s%10
        carry = s/10
    if carry > 0:
        digits.insert(0, carry)
    return digits


#
# Given an array of integers. Find the minimum length subarray
# required to be sorted, such that the whole array becomes sorted.
#
# Input: [2, 4, 7, 5, 3, 9, 11]
# Output: [4, 7, 5, 3]
#
# T(n)- O(n)
#
def minimum_subarray_sort(a):
    n = len(a)
    s, e = 0, n-1

    # Find first index from left where array is becoming unsorted
    while s < n-1:
        if a[s] > a[s+1]:
            break
        s += 1

    if s == n-1:  # Array is completely sorted
        return

    # Find first index from right where array is becoming unsorted
    while e > 0:
        if a[e] < a[e-1]:
            break
        e -= 1

    # At this point, s = 2 and e = 4
    max_sub = max(a[s:e+1])  # max element of subarray- 7
    min_sub = min(a[s:e+1])  # min element of subarray- 3

    # Find first index from left greater than min_sub
    for i in range(s):
        if a[i] > min_sub:
            s = i
            break

    # Find first index from right smaller than max_sub
    for i in range(n-1, e, -1):
        if a[i] < max_sub:
            e = i
            break

    return a[s:e+1]


def main():
    a = list(map(int, raw_input().split()))
    print next_greater_element(a)

if __name__ == '__main__':
    main()
