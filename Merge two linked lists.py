# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head
        
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next = l1
                break
            else:
                smallestvalue = 0
                if l1.val < l2.val:
                    smallestvalue = l1.val
                    l1 = l1.next
                else:
                    smallestvalue = l2.val
                    l2 = l2.next
                newnode = ListNode(smallestvalue)
                ptr.next = newnode
                ptr = ptr.next
        return head.next

