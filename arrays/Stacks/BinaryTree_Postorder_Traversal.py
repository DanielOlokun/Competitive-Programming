 # Given the root of a binary tree, return the POSTORDER traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):

        result = []

        def dfs(node):
            if not node:
                return      #  is the current node = none ,ie, has the end of the branch been reached
            dfs(node.left)  #  go left
            dfs(node.right) #  go right
            result.append(node.val) #  visit root (in postorderly fashion)

        dfs(root)
        return result
