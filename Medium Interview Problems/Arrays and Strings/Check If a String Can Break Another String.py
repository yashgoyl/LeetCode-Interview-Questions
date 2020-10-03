class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        def can(a,b):
            for x,y in zip(a,b):
                if x > y:
                    return False
                
            return True
    
        return can(s1,s2) or can(s2,s1)


obj = Solution()
print(obj.checkIfCanBreak('abc','xya'))
