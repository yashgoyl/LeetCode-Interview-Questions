import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        # s = ''.join(x.lower() for x in s if x.isalnum())
        # return s == s[::-1]

        #----OR----

        s = re.sub('\W+','',s).lower()
        return s == s[::-1]

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))