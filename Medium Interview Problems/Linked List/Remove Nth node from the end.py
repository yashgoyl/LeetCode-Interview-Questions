# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Find the proper index 'k'
        temp = head 
        numnodes = 0
        while temp is not None:
            temp = temp.next
            numnodes += 1
        k = numnodes - n
        
        # Find the proper node to remove
        prev = None
        ptr = head
        while k!=0:
            prev = ptr
            ptr = ptr.next
            k -= 1
            
        # Remove Node
        if prev is None:
            return head.next
        else:
            prev.next = ptr.next
            ptr.next = None
            return head