class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

obj = Solution()
print(obj.strStr('hello','ll'))
