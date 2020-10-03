class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = collections.Counter(nums)
        
        l = len(nums)//2
        
        for i in dic.elements():
            if dic[i] > l:
                return i
            
