# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        head = [4,5,1,9]
        if node in head:
            head.remove(node)
        return head
        
obj = Solution()
print(obj.deleteNode(1))