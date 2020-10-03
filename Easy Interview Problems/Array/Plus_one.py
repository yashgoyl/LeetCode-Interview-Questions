class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        l = []
        for i in digits:
            s = s + str(i)
            
        it = int(s)
        it = it+1
        s1 = str(it)
        for j in s1:
            l.append(j)

        return l
            
obj = Solution()
print(obj.plusOne([1,2,3]))
