
# ************************ N-ary Tree: Level-order Traversal Uplevel *********************************
# DAM 12/5/2021
# Given an binary tree and an integer k, check whether the tree has a root to leaf path
# with a sum of values equal to k.
from collections import deque as queue



class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

def hasPathSum(root, target):

    if (root is None): return False

    hasPathSum = False
    hasPathSumWorker(root, target, 0, hasPathSum)
    return hasPathSum

def hasPathSumWorker(node, target, sum, hasPathSum):

    if (hasPathSum == True):
        return hasPathSum

    if (node.left_ptr is None and node.right_ptr is None):
        if (sum + node.label == target):
            hasPathSum = True
            #return hasPathSum

    # recursion
    if (node.left_ptr != None):
        hasPathSumWorker(node.left_ptr, target, sum + node.label, hasPathSum)

    if (node.right_ptr != None):
        hasPathSumWorker(node.right_ptr, target, sum + node.label, hasPathSum)

# main
A = TreeNode(0)
B = TreeNode(1)
C = TreeNode(2)
D = TreeNode(3)
E = TreeNode(4)
F = TreeNode(5)
G = TreeNode(6)



A.left_ptr = B
A.right_ptr = C
B.left_ptr = D
B.right_ptr = E
#E.left_ptr = D
#E.right_ptr = G

print(hasPathSum(A, 4))

# 2, 5, 4, 0, 1, 3, 6


