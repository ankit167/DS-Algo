#!/usr/bin/python

import sys

def findStartIndex(a, start, end, k):
    if start > end:
        return
    mid = start + (end-start)/2
    if a[mid] == k and (mid == start or a[mid-1] < a[mid]):
        return mid
    elif k <= a[mid]:
        return findStartIndex(a, start, mid-1, k)
    else:
        return findStartIndex(a, mid+1, end, k)

def findEndIndex(a, start, end, k):
    if start > end:
        return
    mid = start + (end-start)/2
    if a[mid] == k and (mid == end or a[mid+1] > a[mid]):
        return mid
    elif k >= a[mid]:
        return findEndIndex(a, mid+1, end, k)
    else:
        return findEndIndex(a, start, mid-1, k)

# find frequency of a number in a sorted array- O(log n) solution
def findOccurances(a, k):
    n = len(a)
    startindex = findStartIndex(a, 0, n-1, k)
    if startindex is None:
        print "Number not Present"
        return
    endindex = findEndIndex(a, startindex, n-1, k)
    print (endindex - startindex) + 1

def findStockSpan(stock, s):
    for i in range(len(stock)-1, -1, -1):
        s[i] = 1
        for j in range(i-1, -1, -1):
            if stock[j] > stock[i]:
                break
            s[i] += 1
    print stock
    print s

# Find max subsequence sum of an array, such that no two elements are adjacent.
def findMaxContSum(a):
    incl,excl = a[0],0
    for i in range(1,len(a)):
        excl_new = max(incl, excl)
        incl = excl + a[i]
        excl = excl_new
    print max(incl, excl)

# DP solution for the same.
def findMaxContSumDP(a):
    s = []
    for i in range(len(a)):
        excl = s[i-1] if i-1 >= 0 else 0
        incl = s[i-2] + a[i] if i-2 >= 0 else a[i]
        s.append(max(incl, excl))
    print s[-1]

class L:
    l = []
    def __init__(self, l):
        self.l = l

def func(O):
    last = len(O) - 1
    while last > 0:
        i,j = 0,last
        while i < j:
            O[i].l = Merge(O[i].l, O[j].l)
            i += 1
            j -= 1
        last = j
    return O[0]


def findString(s):
    vowels = list("aeiou")
    consonants = list("bcdfghjklmnpqrstvwxyz")
    l = []
    for i in range(0,len(s)):
        if s[i] not in vowels:
            continue
        for j in range(i+1,len(s)):
            if s[j] not in consonants:
                continue
            l.append(s[i:j+1])
    l.sort()
    print l[0]
    print l[-1]

def compare(a,b):
    x,y = a + b, b + a
    if x < y:
        return 1
    return -1


def printspir(a,m,n):
    k,l = 0,0
    while k < m and l < n:
        for i in range(l,n):
            print a[k][i],
        k += 1
        for i in range(k,m):
            print a[i][n-1],
        n -= 1
        if k < m:
            for i in range(n-1,l-1,-1):
                print a[m-1][i],
            m -= 1
        if l < n:
            for i in range(m-1,k-1,-1):
                print a[i][l],
            l += 1

def printMaxNumber(s):
    s.sort(compare)
    print s
    #sortedL = sorted(s, cmp=make_comparator(0), reverse=True)
    #return sortedL


def findMinSub(s1,s2):
    min,str = sys.maxint,""
    for i in range(0,len(s1)):
        t, l= "", list(s2)
        for j in range(i,len(s1)):
            if len(l) == 0:
                if len(t) < min:
                    min = len(t)
                    str = t
            t += s1[j]
            if s1[j] in l:
                l.remove(s1[j])
        if len(l) == 0:
            if len(t) < min:
                min = len(t)
                str = t
    print str

def coin(s,m,n):
    n = len(a)
    table = [[0 for i in range(m)] for i in range(n+1)]
    for i in range(m):
        table[0][i] = 1
    for i in range(1,n+1):
        for j in range(m):
            x = table[i][j-1] if j-1 >= 0 else 0
            y = table[i-s[j]][j] if i-s[j] >=0 else 0
            table[i][j] = x + y
    return table[n][m-1]


class SpecialLLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.down = None

class SpecialLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.l = None

    def insert(self,data,direction):
        if self.head == None:
            self.head = SpecialLLNode(data)
            self.tail = self.head
            self.l = self.tail
            return
        if direction == 'right':
            self.tail.next = SpecialLLNode(data)
            self.tail = self.tail.next
            self.l = self.tail
            return
        if direction == 'down':
            self.l.down = SpecialLLNode(data)
            self.l = self.l.down

    def Merge(self,a,b):
        res = None
        if b is None:
            return a
        if a is None:
            return b
        if a.data < b.data:
            res = a
            res.down = self.Merge(a.down,b)
        else:
            res = b
            res.down = self.Merge(a,b.down)
        return res

    def flatten(self,head):
        if head is None or head.next is None:
            return head
        head.next = self.flatten(head.next)
        head = self.Merge(head,head.next)
        return head

    def display(self):
        curr = self.head
        while curr is not None:
            print curr.data,
            curr = curr.down

def main():
    l = list(map(int, raw_input().split()))
    l = [str(x) for x in l]
    l.sort(compare)
    print l

if __name__=='__main__':
    main()


