# class Solution:
#     def gp(self, n):
#         lst = []
#         lst.append(n)
#         while n>0:
#             if n % 2 == 0:
#                 n = n//2
#                 lst.append(n)
#                 if n == 6:
#                     break
#                 elif n < 6:
#                     return "Invalid Input"
#                 else:
#                     continue
#             else:
#                 return "Invalid Input" 
#         s = "It will take "
#         years = str(len(lst))
#         a = " years for the Bamboo tree to reach a height 768 feet."
#         return s + years + a


class Solution:
    def gp(self, value):
        a = 6
        r = 2
        lst = []
        n = 1
        while n > 0:
            b = n-1
            T = a*(r**b)
            lst.append(T)
            if T > value:
                lst.pop()
                break
            else:
                n = n+1
        if value not in lst:
            return 'Invalid Input'
        else:
            s = "It will take "
            years = str(len(lst))
            a = " years for the Bamboo tree to reach a height 768 feet."
            return s + years + a


obj = Solution()
print(obj.gp(768))
print(obj.gp(500))


