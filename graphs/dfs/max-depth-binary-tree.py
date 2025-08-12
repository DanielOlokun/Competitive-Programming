Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#1 --- > Using RECCURSION!!!
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#2 -----> ITERATIVE WAY

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]  # Store (node, depth)

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth
        
