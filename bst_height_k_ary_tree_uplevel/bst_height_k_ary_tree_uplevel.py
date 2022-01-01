# ************************ BST: Height Of K Ary Tree *********************************
# DAM 12/9/2021
# Given a k-ary tree, find the height of that tree: number of edges in the longest path from the root to any node.
# A k-ary tree is a rooted tree in which each node has no more than k children.

class TreeNode():
    def __init__(self):
        self.children = []

def find_height(root):
    # base
    if (root == None): return 0

    if (len(root.children) == 0):
        return 0

    depth = 0

    for child in root.children:
        childDepth = find_height(child) + 1
        
        depth = childDepth if childDepth > depth else depth
        
    return depth


# main
A = TreeNode()
B = TreeNode()
C = TreeNode()
D = TreeNode()
E = TreeNode()
F = TreeNode()
G = TreeNode()

A.children.append(B)
A.children.append(C)
A.children.append(E)
E.children.append(D)
B.children.append(F)
D.children.append(G)


print(find_height(A))