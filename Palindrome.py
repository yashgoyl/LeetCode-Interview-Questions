class Solution:
    def isPalindrome(self, x: int) -> bool:

        # return str(x) == str(x)[::-1]

        #    ------OR------

        y = x
        palin = list()
        if y < 0:
            return False
        while y != 0:
            r = y%10
            palin.append(r)
            y = y//10
        a = int(''.join(str(i) for i in palin)) if x>0 else 0
        print(a)
        print(x)
        if a==x:
            return True
        else:
            return False

b = Solution()
print(b.isPalindrome(0))