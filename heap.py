#!/usr/bin/python

class Heap:
    def __init__(self):
	self.h = []
	self.currsize = 0

    def leftChild(self,i):
	if 2*i+1 < self.currsize:
	    return 2*i+1
	return None

    def rightChild(self,i):
	if 2*i+2 < self.currsize:
	    return 2*i+2
	return None

    def maxHeapify(self,node):
	if node < self.currsize:
	    m = node
	    lc = self.leftChild(node)
	    rc = self.rightChild(node)
	    if lc is not None and self.h[lc] > self.h[m]:
	        m = lc
	    if rc is not None and self.h[rc] > self.h[m]:
	        m = rc
	    if m!=node:
		self.h[node], self.h[m] = self.h[m], self.h[node]
		self.maxHeapify(m)

    def buildHeap(self,a):
	self.currsize = len(a)
	self.h = list(a)
	for i in range(self.currsize/2,-1,-1):
	    self.maxHeapify(i)

    def getMax(self):
        if self.currsize >= 1:
	    me = self.h[0]
            self.h[0], self.h[self.currsize-1] = self.h[self.currsize-1], self.h[0]
	    self.currsize -= 1
	    self.maxHeapify(0)
	    return me
	return None

    #
    # Heap sort on a max heap will return items in ascending order and vice-versa
    #
    def heapSort(self):
        size = self.currsize
	while self.currsize-1 >= 0:
            self.h[0], self.h[self.currsize-1] = self.h[self.currsize-1], self.h[0]
	    self.currsize -= 1
	    self.maxHeapify(0)
        self.currsize = size
        print self.h

    def insert(self,data):
        self.h.append(data)
	curr = self.currsize
	self.currsize+=1
	while self.h[curr] > self.h[curr/2]:
	    self.h[curr], self.h[curr/2] = self.h[curr/2], self.h[curr]
	    curr = curr/2


def main():
    l = list(map(int,raw_input().split()))
    #k = int(raw_input())
    h = Heap()
    h.buildHeap(l)
    #for i in range(k):
    #	print h.getMax()
    h.heapSort()
    h.maxHeapify(0)
    print h.h
    h.insert(50)
    print h.h
    h.heapSort()

if __name__=='__main__':
    main()


