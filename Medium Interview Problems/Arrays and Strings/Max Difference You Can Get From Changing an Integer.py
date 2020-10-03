class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxnum, minnum = float('-inf'), float('inf')
        for a in '0123456789':
            for b in '0123456789':
                nextnum = num.replace(a,b)
                if nextnum[0] == '0' or int(nextnum) == 0:
                    continue
                maxnum = max(maxnum, int(nextnum))
                minnum = min(minnum, int(nextnum))
        return maxnum - minnum

obj = Solution()
print(obj.maxDiff(555))
