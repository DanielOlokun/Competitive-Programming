Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# NB **** --- > WHEN ASKED TO COMPARE BOTH SIDES OF SOMETHING -- > IN THIS CASE A TREE -- > THINK RECURSIVELY !!!!!!


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):

        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, t1, t2):
        if not t1 and not t2:       # here, both nodes are still null --> therefore symettric at this level
            return True
        if not t1 or not t2:
            return False            # here, vals dont match -- > not symmetric

        #checks if children are mirrors of each other
        return (t1.val == t2.val and self.is_mirror(t1.left, t2.right) and self.is_mirror(t1.right, t2.left))
