# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# ITERATIVE VERSION -- > USING POINTERS ---> most optimal version O(n)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):

        curr = head
        prev = None

        while curr:    # while curr not NULL
            next_node = curr.next    # store curr.next in a next_node as we are breaking the pointer form curr to curr.next to reverse it 
            curr.next = prev    
            prev = curr
            curr = next_node

        return prev

  # fyi this quesion can also be solved recirsively 
  # https://www.youtube.com/watch?v=G0_I-ZF0S38
