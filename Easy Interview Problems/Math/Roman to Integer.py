class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        int_val  = 0

        for i in range(len(s)):
            if i>0 and rom_dict[s[i]] > rom_dict[s[i-1]]:
                int_val += rom_dict[s[i]] - 2*rom_dict[s[i-1]]
            else:
                int_val += rom_dict[s[i]]
        return int_val 
            
obj = Solution()
print(obj.romanToInt("MCMXCIV"))