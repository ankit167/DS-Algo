import sys

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class qnode:
    def __init__(self,node,hd):
        self.node = node
        self.hd = hd



class Height:
    def __init__(self):
        self.h = 0


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        newnode = node(data)
        if self.root is None:
            self.root = newnode
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            temp = queue.pop(0)
            if temp.left is None:
                temp.left = newnode
                return
            else:
                queue.append(temp.left)
            if temp.right is None:
                temp.right = newnode
                return
            else:
                queue.append(temp.right)

    #
    # Level order traversal of a tree
    #
    def display(self,root):
        if root is None:
            return
        q = []
        q.append(root)
        while len(q) > 0:
            temp = q.pop(0)
            print temp.data,
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)

    #
    # Checks if a binary tree is a BST. (Inorder way)
    #
    def isBst(self,root,prev=[-sys.maxint-1]):
        if root is None:
            return True
        l = self.isBst(root.left)
        if l is False:
            return False
        if root.data < prev[0]:
            return False
        prev[0] = root.data
        return self.isBst(root.right)

    #
    # Checks if a binary tree is a BST. (Preorder way)
    #
    def checkBst(self, root, minr=-sys.maxint-1, maxr=sys.maxint):
        if root is None:
            return True
        if root.data < minr or root.data > maxr:
            return False
        return (self.checkBst(root.left, minr, root.data) and
                self.checkBst(root.right, root.data, maxr))


    def leftView(self,root,level,maxlevel=[-1]):
        if root is None:
            return
        if level > maxlevel[0]:
            maxlevel[0] = level
            print root.data,
        self.leftView(root.left,level+1)
        self.leftView(root.right,level+1)

    def topView(self):
        if self.root is None:
            return
        q = []
        hashset = set([])
        q.append(qnode(self.root,0))
        while len(q) > 0:
            temp = q.pop(0)
            n = temp.node
            h = temp.hd
            if h not in hashset:
                print n.data,
                hashset.add(h)
            if n.left is not None:
                q.append(qnode(n.left,h-1))
            if n.right is not None:
                q.append(qnode(n.right,h+1))

    def bottomView(self):
        if self.root is None:
            return
        q = []
        hashmap = {}
        q.append(qnode(self.root,0))
        while len(q) > 0:
            temp = q.pop(0)
            n = temp.node
            h = temp.hd
            hashmap[h] = n.data
            if n.left is not None:
                q.append(qnode(n.left,h-1))
            if n.right is not None:
                q.append(qnode(n.right,h+1))
        print [value for (key,value) in sorted(hashmap.items())]

    # prints maximum element in each level
    def maxLevel(self):
        if self.root is None:
            return None
        q = [self.root,None]
        m = -sys.maxint - 1
        while len(q) > 0:
            temp = q.pop(0)
            if temp is None:
                print m
                m = -sys.maxint - 1
                if len(q) > 0:
                    q.append(None)
            else:
                if temp.data > m:
                    m = temp.data
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)

    def height(self,root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        return max(lheight,rheight) + 1

    # Diameter is the longest path between two nodes of a tree
    # which may/may not pass through the root of the tree. O(n^2)
    def diameter(self,root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        ldiameter = self.diameter(root.left)
        rdiameter = self.diameter(root.right)

        return max(lheight+rheight+1,max(ldiameter,rdiameter))

    # O(n) solution. Calculate height along the way as we
    # calculate diameter
    def diameter2(self,root,height):
        lh,rh = Height(),Height()
        if root is None:
            height.h = 0
            return 0
        lh.h+=1
        rh.h+=1
        ldiameter = self.diameter2(root.left,lh)
        rdiameter = self.diameter2(root.right,rh)
        height.h = max(lh.h,rh.h) + 1
        return max(lh.h+rh.h+1,max(ldiameter,rdiameter))

    def diameterOpt(self):
        height = Height()
        return self.diameter2(self.root,height)

    # convert a Binary tree to DLL
    def toDLLUtil(self,root,start=[],prev=[]):
        if root is None:
            return None
        l = self.toDLLUtil(root.left)
        if l is None:
            if len(start) == 0:
                start.append(root)
        if len(prev) > 0:
            prev[0].right = root
            root.left = prev[0]
            prev[0] = root
        else:
            prev.append(root)
        self.toDLLUtil(root.right)
        return start

    def toDLL(self,root):
        head = self.toDLLUtil(root)
        print head[0].data
        curr = head[0]
        while curr is not None and curr.right is not None:
            curr = curr.right
        while curr is not None:
            print curr.data,
            curr = curr.left

    def lca(self,root,n1,n2):
        if root is None:
            return None
        if root.data == n1 or root.data == n2:
            return root
        l = self.lca(root.left,n1,n2)
        r = self.lca(root.right,n1,n2)
        if l is not None and r is not None:
            return root
        elif l is not None:
            return l
        return r

    def printVertical(self,root,h,map):
        if root is None:
            return
        self.printVertical(root.left,h-1,m)
        l = map.get(h,[])
        l.append(root.data)
        map[h] = l
        self.printVertical(root.right,h+1,m)

    def inorderSave(self,root,a):
        if root is None:
            return
        self.inorderSave(root.left,a)
        a.append(root.data)
        self.inorderSave(root.right,a)

    def treeToBstUtil(self,root,a):
        if root is None:
            return
        self.treeToBstUtil(root.left,a)
        root.data = a[0]
        a.pop(0)
        self.treeToBstUtil(root.right,a)

    def displayInorder(self,root):
        if root is None:
            return
        self.displayInorder(root.left)
        print root.data,
        self.displayInorder(root.right)

    def treeToBst(self):
        l = []
        self.inorderSave(self.root,l)
        l.sort()
        self.treeToBstUtil(self.root,l)
        self.displayInorder(self.root)

    def levelOrderTraversalWithoutQueue(self,root):
        h = self.height(root)
        for i in range(h):
            self.displayLevelOrderWithoutQueue(root,i)

    def displayLevelOrderWithoutQueue(self,root,level):
        if root is None:
            return
        if level == 0:
            print root.data,
            return
        self.displayLevelOrderWithoutQueue(root.left,level-1)
        self.displayLevelOrderWithoutQueue(root.right,level-1)

    def mirror(self,root):
        if root is None:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

    #
    # Checks whether two nodes are siblings of each other.
    # Two nodes are said to be siblings of each other, if
    # they have the same parent.
    #
    def isSibling(self, root, a, b):
        if root is None:
            return False
        if (root.left == a and root.right == b) or (root.left == b and root.left == a):
            return True
        return (self.isSibling(root.left, a, b) or
                self.isSibling(root.left, b, a))

    #
    # Returns level number of a node
    #
    def level(self, root, n, level):
        if root is None:
            return 0
        if root == n:
            return level
        l = self.level(root.left, n, level+1)
        if l != 0:
            return l
        return self.level(root.right, n, level+1)

    #
    # Check if two nodes are cousins of each other.
    # Two nodes are said to cousins of each other if
    # they are present at the same level of the Binary
    # tree and have different parents. Two nodes are
    # siblings of each other, if they have the same parent
    # T(n)- O(n)
    #
    def isCousin(self, root, a, b):
        if root is None:
            return None
        if (self.level(root,a,1) == self.level(root,b,1)) and not (self.isSibling(root, a, b)):
           return True
        return False

    #
    # Preorder traversal through iteration.
    # T(n)- O(n), S(n)- O(h)
    # Since traversal is in order- root->root.left->root.right,
    # we first print the root, push root.right followed by
    # root.left in stack.
    #
    def preorderIterative(self, root):
        if root is None:
            return
        st = [root]
        while len(st) > 0:
            temp = st.pop()
            print temp.data,
            if temp.right:
                st.append(temp.right)
            if temp.left:
                st.append(temp.left)

    #
    # Postorder traversal using iteration. (root.left->root.right->root)
    # Idea: Use two stacks. In the end one of the stacks will contain
    #       all the elements in postorder.
    # T(n)- O(n), S(n)- O(n)
    #
    def postorderIterative(self, root):
        if root is None:
            return
        st1, st2 = [root], []
        while len(st1) > 0:
            temp = st1.pop()
            st2.append(temp)
            if temp.left:
                st1.append(temp.left)
            if temp.right:
                st1.append(temp.right)

        while len(st2) > 0:
            temp = st2.pop()
            print temp.data,

    #
    # Remove Half nodes from a tree. Half nodes are nodes that have only
    # one child.
    # T(n)- O(n)
    #
    def removeHalfNodes(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        root.left = self.removeHalfNodes(root.left)
        root.right = self.removeHalfNodes(root.right)
        if root.left is None:
            new_root = root.right
            temp = root
            root = None
            del(temp)
            return new_root
        if root.right is None:
            new_root = root.left
            temp = root
            root = None
            del(temp)
            return new_root
        return root


preindex = 0
def build(preorder,inorder,instart,inend):
    global preindex
    if instart > inend:
        return  None
    newnode = node(preorder[preindex])
    preindex+=1
    if instart == inend:
        return newnode
    index = search(inorder,instart,inend,newnode.data)
    newnode.left = build(preorder,inorder,instart,index-1)
    newnode.right = build(preorder,inorder,index+1,inend)
    return newnode

def search(inorder,instart,inend,data):
    for i in range(instart,inend+1):
        if inorder[i] == data:
            return i

def display(root):
    if root is None:
        return
    display(root.left)
    print root.data,
    display(root.right)


def toBst(a,start,end):
    if start > end:
        return None
    mid = start+(end-start)/2
    newnode = node(a[mid])
    newnode.left = toBst(a,start,mid-1)
    newnode.right = toBst(a,mid+1,end)
    return newnode

if __name__=="__main__":
    a = list(map(int,raw_input().split()))
    t = Tree()
    for i in a:
        t.insert(i)
    #t.xyz()
    t.root = t.removeHalfNodes(t.root)
    t.display(t.root)

