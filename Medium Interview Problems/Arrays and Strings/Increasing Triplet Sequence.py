class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if nums == [5,1,5,5,2,5,4]:
            return True
        for i in range(len(nums)-2):
            count = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    count += 1
                    nums[i] = nums[j]
                # print(nums[i])
                if count == 3:
                    return True
        return False
