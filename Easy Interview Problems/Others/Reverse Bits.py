class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{0:032b}".format(n)[::-1],2)

obj = Solution()
print(obj.reverseBits(11111111111111111111111111111101))
