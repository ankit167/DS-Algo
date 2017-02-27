class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	carry = 0
	def __init__(self):
		self.head = None

    #
    # Insert data at the end.
    #
	def insert(self,data):
		if self.head is None:
			self.head = node(data)
			return
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = node(data)

	#
	# Reverse every k nodes
	# Input: 1->2->3->4->5, k = 2
	# Output: 2->1->4->3->5
	#
	def reverseKNodes(self,head,k):
		curr,prev,nextnode = head,None,None
		i = 0
		while curr is not None and i < k:
			nextnode = curr.next
			curr.next = prev
			prev = curr
			curr = nextnode
			i += 1
		if head is not None:
			head.next = self.reverseKNodes(curr,k)
		return prev

	#
	# Display elements from left to right
	#
	def display(self,head):
		curr = head
		while curr is not None:
			print curr.data,
			curr = curr.next

    #
    # Reverse the nodes.
    # Input: 1->2->3
    # Output: 3->2->1
    #
	def reverse(self,head):
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
	def sumOfLL(self,first,second):
		first = self.reverse(first)
		second = self.reverse(second)
		res,carry = None,0
		while first is not None or second is not None:
			sum = (first.data if first else 0) + (second.data if second else 0) + carry
			carry = sum/10
			temp = node(sum%10)
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
	def multiplyLL(self,first,second):
		curr,sum = first,0
		while curr is not None:
			sum = sum*10 + curr.data
			curr = curr.next
		second = self.reverse(second)
		res,curr,carry = None,second,0
		while curr is not None:
			product = sum * curr.data + carry
			carry = product/10
			temp = node(product%10)
			if res is None:
				res = temp
			else:
				prev.next = temp
			prev = temp
			curr = curr.next
		while carry != 0:
			temp = node(carry%10)
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
	def multiplyLLRecursive(self,first,second):
		curr,sum = first,0
		while curr is not None:
			sum = sum*10 + curr.data
			curr = curr.next
		res = self.mul(sum,second)
		while self.carry != 0:
			temp = node(self.carry%10)
			temp.next = res
			res = temp.
			self.carry = self.carry/10
		return res

	#
	# Utility function to multiply a number with a linked list recursively.
	#
	def mul(self,n,second):
		if second is None:
			return None
		res = self.mul(n,second.next)
		product = n*second.data + self.carry
		self.carry = product/10
		temp = node(product%10)
		temp.next = res
		res = temp
		return res

    #
    # Return total number of nodes present.
    #
	def findLength(self,head):
		if head is None:
			return 0
		curr,n = head,0
		while curr is not None:
			curr = curr.next
			n += 1
		return n

	def sumSameSize(self,first,second):
		res = None
		if first is None:
			return None
		res = self.sumSameSize(first.next,second.next)
		sum = first.data + second.data + self.carry
		self.carry = sum/10
		temp = node(sum%10)
		temp.next = res
		res = temp
		return res

	def sumSameList(self,first,cur):
		if first is None:
			return None
		if first != cur:
			res = self.sumSameList(first.next,cur)
			sum = first.data + self.carry
			self.carry = sum/10
			temp = node(sum%10)
			temp.next = res
			res = temp
			return res
		return None

	# Find sum of two numbers, represented as Linked List- without modifying the lists. T(n)- O(m+n)
	def sumUtil(self,first,second):
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
		res = self.sumSameSize(cur,second)
		res2 = self.sumSameList(first,cur)
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
	def swap_kth(self,head,k):
		n = self.findLength(head):

		if k > n:
			print 'Less Number of nodes'
			return head

		if 2*k - 1 == n:
			return head

		curr,temp = head, None
		for i in range(1,k):
			temp = curr
			curr = curr.next

		kthStart = curr
		kthStartPrev = temp

		curr,temp = head, None
		for i in range(1,n-k+1):
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



def main():
	first = list(map(int,raw_input().split()))
	second = list(map(int,raw_input().split()))
	f = LinkedList()
	s = LinkedList()
	for i in first:
		f.insert(i)
	for i in second:
		s.insert(i)
	res = f.multiply2(f.head,s.head)
	f.display(res)

if __name__ == '__main__':
	main()

