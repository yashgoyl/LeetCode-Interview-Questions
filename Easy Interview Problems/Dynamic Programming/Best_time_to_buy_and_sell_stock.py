class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minimum, maximum = prices[0], 0
        for i in range(1,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                maximum = max(maximum, prices[i]-minimum)
        return maximum

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
