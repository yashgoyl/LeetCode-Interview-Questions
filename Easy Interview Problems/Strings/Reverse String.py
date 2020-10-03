class Solution:
    def reverseString(self, string):
        """
        Time:  O(n)
        Space: O(1)
        """
        i, j = 0, len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return string

obj = Solution()
print(obj.reverseString(['h','e','l','l','o']))