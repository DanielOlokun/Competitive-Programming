Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Definition for a binary tree node.
#class TreeNode(object):
     #def __init__(self, val=0, left=None, right=None):
        #self.val = val
        #self.left = left
        #self.right = right

# i initially tried to return the result like a list but REMEMBER **NB** --> it doesnt accept this as an answer, it needs a root, the way normal tree Qs would

class Solution(object):
    def sortedArrayToBST(self, nums):

        #. recursion

        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])    # use the mid point as the head of the tree
        root.left = self.sortedArrayToBST(nums[:mid])    # call function recursively on the left, then on the right (next line)
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root    # returned as root
