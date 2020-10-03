from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                nums.append(i)
        return nums
                
obj = Solution()
print(obj.intersect([1,2,2,1],[2,2]))