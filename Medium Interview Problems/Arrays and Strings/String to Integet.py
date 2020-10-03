class Solution:
    def myAtoi(self, str):
        if not str:
            return 0
        str = str.lstrip()
        if not str:
            return 0
        
        negative = False
        i = 0
        if str[0] == '+':
            i += 1
        elif str[0] == '-':
            negative = True
            i += 1
        elif not str[0].isdigit():
            return 0

        value = 0
        while i < len(str) and str[i].isdigit():
            value *= 10
            value += int(str[i])
            i += 1
        
        if negative :
            value = -value

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if value < INT_MIN:
            return INT_MIN
        elif value > INT_MAX:
            return INT_MAX
        else:
            return value
obj = Solution()
print(obj.myAtoi("    -42"))



