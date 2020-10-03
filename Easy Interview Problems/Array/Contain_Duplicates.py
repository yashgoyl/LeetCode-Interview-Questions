class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums)
        # print(num)
        for i in num.elements():
            if num[i] > 1:
                return True
            i += 1
        return False

obj = Solution()
print(obj.containDuplicate([1,2,3,1]))
