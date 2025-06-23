# Given the root of a binary tree, return the PREORDER traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):

        stack = []
        result = []
        curr = root

        while curr or stack:
            while curr:        # this keeps going until current node that is null is encountered. ie basically the final node in its 'lineage'      (sorry for the explanation, it made sense in my head :)  )
                result.append(curr.val)    # 'visit' it ie add to result
                stack.append(curr)    # add to stack to monitor it
                curr = curr.left    # attempt to go left -- > brings it back up to while curr to prove if the condition is true 
            curr = stack.pop()  # if it breaks, ie not true, pop rit from stack and goes back to parent node
            curr = curr.right  # attempts to go right

        return result

        
