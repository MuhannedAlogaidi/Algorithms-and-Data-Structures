# ************************ Binary Search Tree: Level-order Traversal Uplevel *********************************
# DAM 12/5/2021
# Given a binary tree, list the label of the nodes, level by level from left to right.
from collections import deque as queue

class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


def level_order_traversal(root):
    result = []

    # edge case
    if (root == None):
        return

    # initialize queue, append the root to the front
    q = queue()
    q.appendleft(root)

    while len(q) > 0:
        # length of queue
        count = len(q)

        # temporary list
        temp = []

        # iterate through queue
        for i in range(0, count):
            tempNode = q.popleft()

            temp.append(tempNode.label)

            #add child nodes to the queue if they exist
            if (tempNode.left_ptr != None):
                q.append(tempNode.left_ptr)

            if (tempNode.right_ptr != None):
                q.append(tempNode.right_ptr)

        result.append(temp)

    return result

# main
A = TreeNode(0)
B = TreeNode(1)
C = TreeNode(2)
D = TreeNode(3)
E = TreeNode(4)
F = TreeNode(5)
G = TreeNode(6)



#C.left_ptr = F
#C.right_ptr = E
#F.left_ptr = A
#F.right_ptr = B
#E.left_ptr = D
#E.right_ptr = G

print(level_order_traversal(C))

# 2, 5, 4, 0, 1, 3, 6

