# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):
intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted

# my FIRST ATTEMPT at solving this question -- > length based----> O(n + m) time , O(1) space

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        # get length of LL ---> move one list to len of other list -- < go from there

        def get_length(head):        # a function to get the lengths of each linked list
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        lenA = get_length(headA)    # call function on both lists
        lenB = get_length(headB)

        currA = headA
        currB = headB

        if lenA > lenB:    # if one list is longer than other, traverse through longer to make sure we have same starting point to intersection
            for _ in range(lenA - lenB):
                currA = currA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA and currB:
            if currA == currB:      # intersection found
                return currA    # intersect
            currA = currA.next
            currB = currB.next

        return None    # if nothing found 

# SECOND ATTEMPT ---->  2 pointer Tech ---> more efficient O(n + m) time, O(1) space

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        if not headA or not headB:        # edge case  --> if both lists are empty
            return None

        currA = headA      # pointers for traversal
        currB = headB

        while currA != currB:      
            currA = currA.next if currA else headB    # keeps going through if currA not at end yet if it is -- > goes to HEAD B ***Nb
            currB = currB.next if currB else headA    # vice versa

        return currA    # here, it either returns none as no intersection found OR ir returns the node they intesected (both in headA and B)




        
