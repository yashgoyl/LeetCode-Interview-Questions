from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(strs==[]):
            return ""

        res =""

        min_len_str = min(len(i) for i in strs)
        
        for i in range(min_len_str):
            temp = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == temp:
                    continue
                else:
                    return res
            res += temp

obj = Solution()
print(obj.longestCommonPrefix(['flower', 'flow', 'flight']))

