class node:
	def __init__(self, data):
		self.data = data
		self.rank = 0
		self.parent = None
		self.child = []

class DisjointSet:
	# map integer to node
	d = {}

	#
	# From a list of n elements, create n disjoint sets
	# Each set has a root node, through which the set is identified.
	# The root node of a set is the node which does not have a parent,
	# i.e., it is parent to itself.
	#
	def createSet(self, l):
		for i in l:
			n = node(i)
			# each node is the parent and child of itself
			n.parent = n
			n.child.append(n)
			self.d[i] = n

	#
	# For two elements belonging to two different sets,
	# merge/join the sets
	#
	def union(self, a, b):
		n1, n2 = self.d.get(a, None), self.d.get(b, None)
		# case where one or both elements are not present in the sets
		if n1 is None or n2 is None:
			return
		# find root nodes of the sets, the elements belong to
		p1, p2 = self.findRoot(n1), self.findRoot(n2)
		# if either of the roots is None or both elements
		# have the same root, then there is no case of join.
		if p1 is None or p2 is None or p1 == p2:
			return
		if p1.rank >= p2.rank:
			# JOIN. make p1 the parent of p2. p2 and its children
			# are now children of p1
			p2.parent = p1
			p1.child = p1.child + p2.child
			# in case of same rank, rank of the root of the merged set
			# is incremented by 1
			if p1.rank == p2.rank:
				p1.rank += 1
		else:
			p1.parent = p2
			p2.child = p2.child + p1.child

    #
    # Find root node of the set, the element belongs to.
    # If element is not root, then recurse to find the root node.
    # Here, along the recursion, we are performing path compression, to reduce
    # the depth of a node from the root node. In the end of the recursion, each
    # node in the recursion will point to the root node of the set, instead of
    # its immediate parent.
    #
    # By reducing the depth of the tree, path compression saves time in finding
    # the root node from a given element
    #
	def findRoot(self, n):
		if n is None:
			return None
		if n.parent == n:
			return n
		n.parent = self.findRoot(n.parent)
		return n.parent

	#
	# Check if two elements belong to the same set.
	# Logic: if they have the same root, then they belong to the same set.
	#
	def checkSameSet(self, a, b):
		n1, n2 = self.d.get(a, None), self.d.get(b, None)
		if n1 is None or n2 is None:
			return False
		p1, p2 = self.findRoot(n1), self.findRoot(n2)
		if p1 is None or p2 is None:
			return False
		if p1 == p2:
			return True
		return False

    #
    # Print all distinct disjoint sets
    #
	def printSets(self):
		for node in self.d.values():
			if node.parent == node:
				for child in node.child:
					print child.data,
				print

def main():
	l = list(map(int, raw_input().split()))
	ds = DisjointSet()
	ds.createSet(l)
	m = int(raw_input())
	for i in range(m):
		a,b = map(int, raw_input().split())
		ds.union(a,b)
	print ds.checkSameSet(2,7)
	ds.printSets()

if __name__ == '__main__':
	main()
