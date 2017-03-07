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

def main():
	a = list(map(int,raw_input().split()))
	minMissing(a)

if __name__=='__main__':
	main()

