You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
       
# n -- > node from end of list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode() # use a dummynode whenevever you need to modify or remove/delete
        dummy.next = head

        slow = fast = dummy

        for _ in range(n + 1):    # to get fast to move n times seach time
            if fast:
                fast = fast.next
            else:
                return head

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next    # when encountering the node to be removed, redirecting pointer to next node

        return dummy.next
    

