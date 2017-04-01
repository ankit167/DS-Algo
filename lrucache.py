'''
Following is a LRU (Least Recently Used) Cache implementation, using
a Doubly Linked List and a Dictionary.

Note:
Changes for MRU (Most Recently Used) Cache
Instead of removeFront(), implement removeBack() (Remove the tail of the
Linked List), since least recently used element is at the front of the
linked list and most recently used element is at the end of the linked list.

Changes for FIFO (First In First Out) Cache
If element is already present in cache, there is no adjustment of pointers
required. Keep the linked list as is. So, skip writing the adjust().

T(n)- O(n), n is number of queries.
'''
class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    head = None
    tail = None

    # Inserts at the end of the Linked List
    def insertEnd(self, newnode):
        if self.head is None:
            self.head = newnode
            self.tail = self.head
            return
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    # Removes the head of the Linked List
    def removeFront(self):
        if self.head is None:
            return None
        t = self.head
        p = self.head.next
        self.head.next = None
        if p:
            p.prev = None
        self.head = p
        return t

    # Removes the current node and inserts it at the end
    def adjust(self, n):
        if n is None or n == self.tail:
            return
        if n == self.head:
            t = self.removeFront()
            self.insertEnd(t)
            return
        # node is neither head nor tail
        p,t = n.prev, n.next
        n.prev, n.next = None, None
        if p:
            p.next = t
        if t:
            t.prev = p
        self.insertEnd(n)

    def display(self):
        curr = self.head
        while curr is not None:
            print curr.data,
            curr = curr.next
        print

class LRU:
    def __init__(self, maxsize, dll):
        self.currsize = 0
        # maxsize of cache
        self.maxsize = maxsize
        self.dll = dll
        self.hmap = {}

    def insert(self, data):
        # if data in hmap => data is present in cache
        if data in self.hmap:
            self.dll.adjust(self.hmap[data])
            self.dll.display()
            return
        # data not present in cache
        newnode = node(data)
        # if cache is full, remove lru node and then insert
        if self.currsize >= self.maxsize:
            t = self.dll.removeFront()
            self.hmap.pop(t.data)
            self.currsize -= 1
        self.dll.insertEnd(newnode)
        self.hmap[data] = newnode
        self.currsize += 1
        self.dll.display()

def main():
    maxsize = int(raw_input())
    l = list(map(int, raw_input().split()))
    dll = DLL()
    lru = LRU(maxsize, dll)
    for i in l:
        lru.insert(i)

if __name__ == '__main__':
    main()
