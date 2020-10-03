import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        # print(counter)
        for i in counter:
            print(i)
            if counter[i] == 1:
                # print(counter[i])
                index = s.find(i)
                # print(index)
                return index
                break
        return -1

obj = Solution()
print(obj.firstUniqChar("loveleetcode"))