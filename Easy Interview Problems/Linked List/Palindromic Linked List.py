# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        temp = head
        if temp == None or temp.next == None:
            return True
        while temp is not None:
            lst.append(temp)
            temp = temp.next
            
        return lst == lst.reverse()

obj = Solution()
print(obj.isPalindrome([1,2]))