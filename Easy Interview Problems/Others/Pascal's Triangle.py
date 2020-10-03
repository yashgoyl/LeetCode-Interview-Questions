class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(numRows):
            res = [1]*(i+1)
            for i in range(1,i):
                for j in range(i,0,-1):
                    res[j] += res[j-1]
            lst.append(res)
        return lst

obj = Solution()
n = int(input())
print(obj.generate(n))
