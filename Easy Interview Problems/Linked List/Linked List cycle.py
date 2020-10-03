# Definition for singly

# Example 2:-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        fast, slow = head, head
        
        while fast and fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
            
            if fast == slow:
                return True
        return False
