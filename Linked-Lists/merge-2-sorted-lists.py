# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()      # start off with a dummy node
        curr = dummy    # set curr = this dummy node

        while list1 and list2:    # while neither  list is empty
            if list1.val < list2.val:    # takes list which has the lowest first value and goes from there to start etc ...
                curr.next = list1    # next node = list 1 node
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2    # when no other element in one of lists, return other

        return dummy.next      # return statement
        
