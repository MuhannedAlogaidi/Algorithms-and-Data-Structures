# ************************ BST: K-th Smallest Element of BST *********************************
# DAM 12/9/2021
# Given a binary search tree (BST) and an integer k, find k-th smallest element.

class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


def kth_smallest_element(root, k):
    if (root is None): return 0

    nodeStack = []
    node = root

    while (node != None or len(nodeStack) > 0):
        while (node != None):
            nodeStack.append(node)
            node = node.left_ptr

        node = nodeStack.pop()

        # in order traversal
        k -= 1
        if (k ==0): return node.label
        node = node.right_ptr

    return 0


