# ************************ N-ary Tree: Level-order Traversal Uplevel *********************************
# DAM 12/5/2021
# Given an N-ary tree, list the labels of the nodes, level by level from left to right.
from collections import deque as queue

class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.children = []

def level_order(root):
    result = []

    # edge case
    if (root == None):
        return

    # initialize queue, append the root to the front
    q = queue()
    q.appendleft(root)

    # iterate over tree
    while len(q) > 0:
        # length of queue
        count = len(q)

        # temporary list
        temp = []

        # iterate through queue: 
        # process the nodes at the current level
        for i in range(0, count):
            tempNode = q.popleft()

            temp.append(tempNode.label)

            # get the level below for the next loop:
            # add child nodes to the queue if they exist
            for child in tempNode.children:
                q.append(child)

        result.append(temp)


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


