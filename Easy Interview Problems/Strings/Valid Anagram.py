class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = [s[i] for i in range(len(s))]
        a = sorted(sl)
        # print(a)
        tl = [t[j] for j in range(len(t))]
        b = sorted(tl)
        if a == b:
            return True
        else:
            return False

obj = Solution()
print(obj.isAnagram('a','b'))