class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        sum_result = [0 for i in range(len(nums))]
        sum_result[0] = nums[0]
        for i in range(1,len(nums)):
            if sum_result[i-1] < 0:
                sum_result[i] = nums[i]
            else:
                sum_result[i] = sum_result[i-1] + nums[i]
        return max(sum_result)

obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
