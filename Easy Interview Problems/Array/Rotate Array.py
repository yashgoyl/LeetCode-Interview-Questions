class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < 0:
            return 0
        for i in range(0,k):
            num = nums.pop()
            nums.insert(0,num)
        return nums

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7],3))
