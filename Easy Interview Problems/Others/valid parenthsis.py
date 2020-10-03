class Solution:
    def isValid(self, s: str) -> bool:    
        stack = []
        clos_dict = {"}": "{", "]": "[", ")": "("}

        for i in s:
            if i in clos_dict:
                if len(s) == 0 or clos_dict[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return len(stack) == 0

obj = Solution()
print(obj.isValid(""))