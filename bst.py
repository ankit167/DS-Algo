class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Bst:
	def __init__(self):
		self.root = None

	def insert(self,root,data):
		if root is None:
			root = node(data)
			return root
		elif data <= root.data:
			root.left = self.insert(root.left,data)
		else:
			root.right = self.insert(root.right,data)
		return root

	def lca(self,root,n1,n2):
		if root is None:
			return None
		if root.data > n1 and root.data > n2:
			return self.lca(root.left,n1,n2)
		if root.data < n1 and root.data < n2:
			return self.lca(root.right,n1,n2)
		return root

def main():
	a = list(map(int,raw_input().split()))
	t = Bst()
	for i in a:
		t.root = t.insert(t.root,i)
	n1,n2 = map(int,raw_input().split())
	node = t.lca(t.root,n1,n2)
	print node.data

if __name__ == '__main__':
	main()
