class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    carry = 0

    def __init__(self):
        self.head = None

    #
    # Insert data at the end.
    #
    def insert(self, data):
        if self.head is None:
            self.head = node(data)
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node(data)

    #
    # Reverse every k nodes
    # Input: 1->2->3->4->5->6->7, k = 3
    # Output: 3->2->1->6->5->4->7
    #
    def reverseKNodes(self, head, k):
        curr, prev, nextnode = head, None, None
        i = 0
        while curr is not None and i < k:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
            i += 1
        if head is not None:
            head.next = self.reverseKNodes(curr, k)
        return prev

    #
    # Reverse elements in blocks of 2
    # Input: 1->2->3->4->5
    # Output: 2->1->4->3->5
    #
    def reverse_two_nodes(self, head):
        if not head or not head.next:
            return head

        n = head.next
        p = n.next
        n.next = head
        head.next = self.reverse_two_nodes(p)
        return n

    #
    # Display elements from left to right
    #
    def display(self, head):
        curr = head
        while curr is not None:
            print curr.data,
            curr = curr.next

    #
    # Reverse the nodes.
    # Input: 1->2->3
    # Output: 3->2->1
    #
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        p = head.next
        head.next = None
        revrest = self.reverse(p)
        p.next = head
        return revrest

    #
    # Add two numbers, each being represented as a Singly Linked List.
    # T(n)- O(m+n)
    # Reverse each list-->Add-->Reverse the resultant list.
    # Note: The original lists are being modified.
    #
    def sumOfLL(self, first, second):
        first = self.reverse(first)
        second = self.reverse(second)
        res, carry = None, 0
        while first is not None or second is not None:
            sum = (first.data if first else 0) + (second.data if second else 0) + carry
            carry = sum/10
            temp = node(sum % 10)
            if res is None:
                res = temp
            else:
                prev.next = temp
            prev = temp
            if first:
                first = first.next
            if second:
                second = second.next
        if carry != 0:
            prev.next = node(carry)
        res = self.reverse(res)
        return res

    #
    # Multiply two numbers represented as a Linked List. T(n)- O(m+n)
    # Consolidate the first list to a number-->Reverse second list-->Multiply-->Reverse resultant list
    # Note: One the Linked List gets modified.
    #
    def multiplyLL(self, first, second):
        curr, sum = first, 0
        while curr is not None:
            sum = sum*10 + curr.data
            curr = curr.next
        second = self.reverse(second)
        res, curr, carry = None, second, 0
        while curr is not None:
            product = sum * curr.data + carry
            carry = product/10
            temp = node(product % 10)
            if res is None:
                res = temp
            else:
                prev.next = temp
            prev = temp
            curr = curr.next
        while carry != 0:
            temp = node(carry % 10)
            prev.next = temp
            prev = temp
            carry = carry/10

        res = self.reverse(res)
        return res

    #
    # Multiply two numbers represented as a Linked List. T(n)- O(m+n)
    # Consolidate the first list to a number-->Multiply with second list recursively.
    # Note: This solution works WITHOUT any modification to any of the Linked Lists.
    #
    def multiplyLLRecursive(self, first, second):
        curr, sum = first, 0
        while curr is not None:
            sum = sum*10 + curr.data
            curr = curr.next
        res = self.mul(sum, second)
        while self.carry != 0:
            temp = node(self.carry % 10)
            temp.next = res
            res = temp
            self.carry = self.carry/10
        return res

    #
    # Utility function to multiply a number with a linked list recursively.
    #
    def mul(self, n, second):
        if second is None:
            return None
        res = self.mul(n, second.next)
        product = n*second.data + self.carry
        self.carry = product/10
        temp = node(product % 10)
        temp.next = res
        res = temp
        return res

    #
    # Return total number of nodes present.
    #
    def findLength(self, head):
        if head is None:
            return 0
        curr, n = head, 0
        while curr is not None:
            curr = curr.next
            n += 1
        return n

    def sumSameSize(self, first, second):
        res = None
        if first is None:
            return None
        res = self.sumSameSize(first.next, second.next)
        sum = first.data + second.data + self.carry
        self.carry = sum/10
        temp = node(sum % 10)
        temp.next = res
        res = temp
        return res

    def sumSameList(self, first, cur):
        if first is None:
            return None
        if first != cur:
            res = self.sumSameList(first.next, cur)
            sum = first.data + self.carry
            self.carry = sum/10
            temp = node(sum % 10)
            temp.next = res
            res = temp
            return res
        return None

    # Find sum of two numbers, represented as Linked List- without modifying the lists. T(n)- O(m+n)
    def sumUtil(self, first, second):
        n1 = self.findLength(first)
        n2 = self.findLength(second)
        if n1 >= n2:
            diff = n1 - n2
        elif n2 > n1:
            diff = n2 - n1
            temp = first
            first = second
            second = temp
        cur = first
        while diff > 0:
            cur = cur.next
            diff -= 1
        res = self.sumSameSize(cur, second)
        res2 = self.sumSameList(first, cur)
        t = res2
        while res2 is not None and res2.next is not None:
            res2 = res2.next
        if res2 is not None:
            res2.next = res
        res = t if t is not None else res
        if self.carry != 0:
            temp = node(self.carry)
            temp.next = res
            res = temp
        return res

    #
    # Swap the kth element from the beginning and the end of a linked list
    #
    def swap_kth(self, head, k):
        n = self.findLength(head)
        if k > n:
            print 'Less Number of nodes'
            return head

        if 2*k - 1 == n:
            return head

        curr, temp = head, None
        for i in range(1, k):
            temp = curr
            curr = curr.next

        kthStart = curr
        kthStartPrev = temp

        curr, temp = head, None
        for i in range(1, n-k+1):
            temp = curr
            curr = curr.next

        kthEnd = curr
        kthEndPrev = temp
        if kthStartPrev:
            kthStartPrev.next = kthEnd
        if kthEndPrev:
            kthEndPrev.next = kthStart
        temp = kthStart.next
        kthStart.next = kthEnd.next
        kthEnd.next = temp

        if k == 1:
            head = kthEnd
        if k == n:
            head = kthStart
        return head

    #
    # This function removes duplicates entries from the linked list (unsorted).
    # Input: 1->2->1->3->2, Output: 1->2->3
    # Approaches:
    # (a) Naive- for each element, traverse, check duplicates and adjust pointers
    #            T(n)- O(n^2)
    # (b) Use Hashset (Discussed below)- Hash each unique element in the list,
    #                  and remove elements if they are already present in the
    #                  Hashset. T(n)- O(n), S(n)- O(n)
    # Note: In a sorted linked list, this can be done in O(n) time.
    #       (No extra space)
    #
    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        hset = set()
        hset.add(curr.data)
        while curr is not None:
            temp = curr.next
            while temp is not None and temp.data in hset:
                temp = temp.next
            if temp:
                hset.add(temp.data)
            curr.next = temp
            curr = temp
        return head

    #
    # Merge two linked lists alternately
    # a: 1->2->3, b: 4->5->6
    # Output: 1->4->2->5->3->6
    # T(n)- O(m+n)
    #
    def mergeAlt(self, a, b, turn=0):
        if a is None:
            return b
        if b is None:
            return a
        if turn == 0:
            res = a
            res.next = self.mergeAlt(a.next, b, 1-turn)
        else:
            res = b
            res.next = self.mergeAlt(a, b.next, 1-turn)
        return res

    #
    # Input: 1->3->2->7->4->9
    # Output: 1->9->3->4->2->7
    # Approach: (i) Reach the mid of the linked list (Use slow and fast method)
    #           (ii) Reverse the second half of the linked list
    #           (iii) Merge the two lists alternately
    # T(n)- O(n)
    #
    def fold_list(self, head):
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p = slow.next
        slow.next = None
        p = self.reverse(p)
        head = self.mergeAlt(head, p)
        return head

    #
    # Given a linked list, and only a pointer to a node. Delete the node.
    # Approach: Copy the next node's data to the current node. Delete the
    #           the next node, by adjusting pointers.
    # Input: 1->2->3->4, p- pointer to 3
    # Output: 1->2->4
    #
    # T(n)- O(1)
    #
    # Note: The solution would not work if the node is the last node of the
    #       linked list. For the solution to work, we need to modify the
    #       structure of the linked list, and make the last node as dummy node
    #
    def delete_with_a_single_pointer(self, p):
        if p is None or p.next is None:
            return
        t = p.next
        p.data = t.data  # Copying next node's data to given node
        p.next = t.next  # Adjusting pointers
        t.next = None
        del t  # Deleting the next node.

    #
    # Given a linked list of 0s and 1s. Sort the linked list
    # (by rearranging the pointers), such that all 0s are at
    # the beginning and all 1s are at the end.
    #
    def sort_list_of_0s_and_1s(self):
        if not self.head or not self.head.next:
            return

        curr = self.head
        first_zero, first_one = None, None
        curr_zero, curr_one = None, None

        while curr:
            if curr.data == 0:
                if not first_zero:
                    first_zero = curr
                else:
                    curr_zero.next = curr
                curr_zero = curr

            else:
                if not first_one:
                    first_one = curr
                else:
                    curr_one.next = curr
                curr_one = curr

            curr = curr.next

        if curr_zero:
            curr_zero.next = first_one
        if curr_one:
            curr_one.next = None

        if first_zero:
            self.head = first_zero
        else:
            self.head = first_one


def main():
    l = list(map(int, raw_input().split()))
    f = LinkedList()
    for i in l:
        f.insert(i)
    f.sort_list_of_0s_and_1s()
    f.display(f.head)

if __name__ == '__main__':
    main()
