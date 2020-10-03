class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x *= sign

        while x:
            if x%10 == 0:
                x //= 10
            else:
                break
        
        x = str(x)
        lst = list(x)
        lst.reverse()
        x = "".join(lst)
        a = int(x)
        if a > 2147483647:
            return 0
        elif a < -2147483648:
            return 0
        else:
            return sign*a

        #sign = False
        #result = None
        #if x < 0:
            #sign = True
            #x = abs(x)
#            
        #x_str = str(x)
#        
        #if sign:
            #result = '-' + x_str[::-1]
        #else:
            #result = x_str[::-1]
#            
        #output_int = int(result)
#        
        #if output_int > 2147483647:
            #return 0
        #elif output_int < -2147483648:
            #return 0
        #else:
            #return output_int
a = Solution()
print(a.reverse(1534236469))
            