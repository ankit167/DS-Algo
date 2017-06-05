class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, *args):
        self.head = None if args is None else args[0]

    def insert(self, data):
        if self.head is None:
            self.head = node(data)
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        newnode = node(data)
        curr.next = newnode
        newnode.prev = curr

    def reverse(self, head):
        if head is None:
            return head
        if head.next is None:
            temp = head.next
            head.next = head.prev
            head.prev = temp
            return head
        p = head.next
        head.next = None
        revrest = self.reverse(p)
        p.next = head
        head.prev = p
        return revrest

    def display(self):
        curr = self.head
        while curr is not None:
            temp = curr
            print curr.data,
            curr = curr.next
        print
        while temp is not None:
            print temp.data,
            temp = temp.prev

    #
    # Check if a pair of elements is present in a sorted DLL,
    # the sum of which is 'k'. T(n)- O(n)
    #
    def findSumPair(self, head, k):
        if head is None:
            return False
        tail = head
        while tail.right is not None:
            tail = tail.right
        i, j = head, tail
        while i and j and i.data < j.data:
            temp = i.data + j.data
            if temp == k:
                return True
            elif temp < k:
                i = i.right
            else:
                j = j.left
        return False


def main():
    first = list(map(int, raw_input().split()))
    dll = DoublyLinkedList()
    for i in first:
        dll.insert(i)
    dll.head = dll.reverse(dll.head)
    dll.display()


if __name__ == '__main__':
    main()
