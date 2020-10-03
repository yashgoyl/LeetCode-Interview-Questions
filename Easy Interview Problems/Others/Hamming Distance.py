class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

obj = Solution()
print(obj.hammingDistance(1,4))
