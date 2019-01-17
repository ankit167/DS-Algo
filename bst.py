from dll import DoublyLinkedList as dll
from tree import Tree as tree


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            root = node(data)
            return root
        elif data <= root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    #
    # Return maximum element of the BST.
    #
    def get_max(self, root):
        if root is None:
            return None

        if root.right is None:
            return root

        return self.get_max(root.right)

    #
    # Delete a node in the BST
    # T(n)- O(log n)
    #
    def delete_node(self, root, data):
        if root is None:
            return None

        if data < root.data:
            root.left = self.delete_node(root.left, data)

        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left and root.right:
                temp = self.get_max(root.left)
                root.data = temp.data
                root.left = self.delete_node(root.left, temp.data)
            else:
                temp = root
                if not temp.left:
                    root = temp.right
                if not temp.right:
                    root = temp.left
                del(temp)
        return root

    #
    # Find the least common ancestor of two nodes in a BST
    # T(n)- O(h). (Also refer to finding lca using parent pointers in gfg)
    #
    def lca(self, root, n1, n2):
        if root is None:
            return None
        if root.data > n1 and root.data > n2:
            return self.lca(root.left, n1, n2)
        if root.data < n1 and root.data < n2:
            return self.lca(root.right, n1, n2)
        return root

    def inorderAppend(self, a, root):
        if root is None:
            return
        self.inorderTraversal(a, root.left)
        a.append(root.data)
        self.inorderTraversal(a, root.right)

    #
    # Converts a BST into a Doubly Linked List and
    # returns the head of the new DLL.
    # T(n)- O(n)
    #
    def convertToDLL(self, root, start=[None], prev=[None]):
        if root is None:
            return None
        self.convertToDLL(root.left)
        root.left = prev[0]
        if prev[0]:
            prev[0].right = root
        else:
            start[0] = root
        prev[0] = root
        self.convertToDLL(root.right)
        return start[0]

    #
    # Check for a pair of numbers in the BST, the sum of which is 'k'
    # Approaches-
    # (a) Do inorder traversal->store element in an array->we have a sorted
    #     array-> Check for pairs in the array. T(n)- O(n), S(n)- O(n)
    # (b) Convert the BST into a Doubly Linked List-> The DLL is sorted->
    #     Check for pairs using two pointers in the DLL. T(n)- O(n)
    #     However, this approach modifies the BST.
    # (c) Do inorder and reverse inorder parallely using loop. Check for
    #     left most and right most element of the tree, and move accordingly
    #     T(n)- O(n), S(n)- O(log n). Does not modify the BST.
    # Approach (c) is discussed below
    #
    def sumK(self, root, k):
        if root is None:
            return
        stack1, stack2 = [], []
        flag1, flag2 = True, True
        curr1, curr2 = root, root
        while(True):
            while(flag1):
                if curr1:
                    stack1.append(curr1)
                    curr1 = curr1.left
                else:
                    if len(stack1) == 0:
                        flag1 = False
                    else:
                        curr1 = stack1.pop()
                        val1 = curr1.data
                        curr1 = curr1.right
                        flag1 = False
            while(flag2):
                if curr2:
                    stack2.append(curr2)
                    curr2 = curr2.right
                else:
                    if len(stack2) == 0:
                        flag2 = False
                    else:
                        curr2 = stack2.pop()
                        val2 = curr2.data
                        curr2 = curr2.left
                        flag2 = False
            if val1 >= val2:
                return False
            if val1 + val2 == k:
                return True
            elif val1 + val2 < k:
                flag1 = True
            elif val1 + val2 > k:
                flag2 = True

    #
    # Utility function to find the inconsistent nodes to be swapped.
    #
    def correct_bst_util(self, root, first, mid, last, prev):
        if root is None:
            return
        self.correct_bst_util(root.left, first, mid, last, prev)
        if prev[0] and root.data < prev[0].data:
            if not first[0]:
                first[0] = prev[0]
                mid[0] = root
            else:
                last[0] = root  # It is sure that the nodes are non-adjacent
        prev[0] = root
        self.correct_bst_util(root.right, first, mid, last, prev)

    #
    # Two nodes in a BSt are swapped. Fix and correct the BST
    # Approach 1: Create and auxilliary array. Store inorder traversal.
    #             Sort the array. Recreate the BST from the sorted array.
    #             T(n)- O(nlogn) + O(n) ~ O(nlogn)   S(n)- O(n)
    #
    # Approach 2: Do inorder traversal of the BST. In a correct BST, every
    #             node will be greater than the previous node. Using this idea,
    #             find the inconsistent nodes and store their addresses. In the
    #             end, swap the data of the nodes.
    #             T(n)- O(n)
    #
    def correct_bst(self, root):
        t = tree()
        t.displayInorder(root)  # using this method from tree.py
        print
        first, mid, last, prev = [None], [None], [None], [None]
        self.correct_bst_util(root, first, mid, last, prev)
        # There can be two cases.
        # Case 1: The two nodes are non-adjacent to each other in the traversal
        # In this case, we would swap first and last
        if first[0] and last[0]:
            first[0].data, last[0].data = last[0].data, first[0].data
        # Case 2: The two nodes are adjacent to each other in the traversal
        # In this case, last[0] is None, and we would swap first and mid
        elif first[0] and mid[0]:
            first[0].data, mid[0].data = mid[0].data, first[0].data
        t.displayInorder(root)

    #
    # Modify a BST in such a way that each node stores the sum of all nodes
    # greater than the current node
    #
    def store_sum_of_larger_nodes(self, root, sumK=[0]):
        if root is None:
            return
        self.store_sum_of_larger_nodes(root.right)
        temp = root.data
        root.data = sumK[0]
        sumK[0] += temp
        self.store_sum_of_larger_nodes(root.left)

    #
    # Find minimum absolute difference between any two nodes of a BST
    # Approach: The minimum absolute difference possible can only be found
    #           between two adjacent nodes, in an inorder traversal of the BST.
    #
    # T(n)- O(n)
    #
    def min_absolute_difference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_min_abs_diff(root, prev, min_diff):
            if not root:
                return None
            find_min_abs_diff(root.left, prev, min_diff)
            if prev[0] is not None:
                diff = root.val - prev[0].val
                if not min_diff[0] or diff < min_diff[0]:
                    min_diff[0] = diff
            prev[0] = root
            find_min_abs_diff(root.right, prev, min_diff)

        prev, min_diff = [None], [None]
        find_min_abs_diff(root, prev, min_diff)
        return min_diff[0]


def main():
    a = list(map(int, raw_input().split()))
    t = Bst()
    for i in a:
        t.root = t.insert(t.root, i)
    tr = tree()
    t.store_sum_of_larger_nodes(t.root)
    tr.displayInorder(t.root)


if __name__ == '__main__':
    main()
