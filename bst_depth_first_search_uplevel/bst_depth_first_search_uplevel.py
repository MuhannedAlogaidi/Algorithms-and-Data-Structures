# ************************ Binary Search Tree: Depth-first Search, Pre-order Traversal Uplevel *********************************
# DAM 12/5/2021
# Given a binary tree, find the pre-order traversal of its node's labels.

class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


def preorder(root):
    list = []

    preOrderTraversalWorker(root, list)

    return list

def preOrderTraversalWorker(root, results):
    # base case
    if root is None:
        return

    # recursive case
    # pre-order processing
    results.append(root.label)

    if root.left_ptr is not None:
        preOrderTraversalWorker(root.left_ptr, results)

    if root.right_ptr is not None:
        preOrderTraversalWorker(root.right_ptr, results)

# main
A = TreeNode(0)
B = TreeNode(1)
C = TreeNode(2)
D = TreeNode(3)
E = TreeNode(4)

A.left_ptr = B
A.right_ptr = C
B.left_ptr = D
B.right_ptr = E

print(preorder(A))
