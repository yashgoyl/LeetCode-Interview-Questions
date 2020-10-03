from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = nums.sort()
        a = [nums[i] for i in range(len(nums)) if nums[i] != nums[i-1] ]
        return len(a)

        # if not nums:
        #     return 0
        # C= collections.Counter(nums)      # first import collections
        # print(C)
        # nums[:] = [i for i in C]
        # return len(nums)

obj = Solution()
print(obj.removeDuplicates([1,1,1,2,2,1,3,2,2,1,0,3]))   
