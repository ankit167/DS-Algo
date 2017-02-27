#!/usr/bin/python

from collections import deque

#
# Find minimum in each 'k' sized window. (Deque approach)
#
def func(a,k):
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
# Search a key in a row wise and column wise sorted matrix. O(m+n)
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
# T(n)- O(logn). Binary Search, since the array is sorted
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

def main():
	l = list(map(int,raw_input().split()))
	print findStartOne(l,0,len(l)-1)

if __name__=='__main__':
	main()

#12 3 4 10 6 5
# k =4
# 12 10 10
