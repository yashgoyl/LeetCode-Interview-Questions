class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
                i = i+1
        return nums

obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))
