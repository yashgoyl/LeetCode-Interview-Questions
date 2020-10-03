class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

obj = Solution()
print(obj.hammingWeight(00000000000000000000000010000000))
