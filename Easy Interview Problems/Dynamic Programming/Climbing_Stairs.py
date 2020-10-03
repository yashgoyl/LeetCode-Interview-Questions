class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return n
        else:
            a,b,c = 0,1,2
            for i in range(2,n):
                a = b + c
                b = c
                c = a
            return a

obj = Solution()
print(obj.climbStairs(5))
