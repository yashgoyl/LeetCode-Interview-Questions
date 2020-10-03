from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                j+=1
            i+=1

obj = Solution()
print(obj.twoSum([2,7,15,19],9))