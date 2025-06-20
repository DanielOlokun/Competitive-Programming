# Given the root of a binary tree, return the INORDER traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):

        result = []
        stack = []
        curr = root    # initialise curr as root

        while curr or stack:    # while curr is not NULL and stack is not empty
            while curr:    # while curr not NULL
                stack.append(curr)
                curr = curr.left    # once this loop exits, this means curr is now NULL
            curr = stack.pop()
            result.append(curr.val)    
            curr = curr.right    # shift to right

        return result            
        
