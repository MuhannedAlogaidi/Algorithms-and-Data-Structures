# ************************ BST: Balanced Tree From Sorted Array *********************************
# DAM 12/9/2021
# Given N distinct integers in a sorted array, build a balanced binary search tree.
class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

def arrayToBST(arr):
    return arrayToBSTWorker(arr, 0, len(arr) - 1)

def arrayToBSTWorker(array, start, end):
    # edge
    if (start > end): return None

    # midpoint
    midpoint = int(start + (end - start)/2)

    # create node with mid
    root = TreeNode(array[midpoint])

    # create left node/subtree
    root.left_ptr = arrayToBSTWorker(array, start, midpoint - 1)

    # create right node/subree
    root.right_ptr = arrayToBSTWorker(array, midpoint + 1, end)

    return root

print(arrayToBST([8, 10, 12, 15, 16, 20, 25]))