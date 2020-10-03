class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
        
        lpsend = 0
        lpsstart = 0
        
        for i in range(n):
            start = i
            end = i
            
            while start >= 0:
                
                #case 1
                if start == end:
                    dp[start][end] = True
                    
                #case 2
                elif start+1 == end:
                    dp[start][end] = s[start] == s[end]
                
                #case 3
                else:
                    dp[start][end] = dp[start+1][end-1] and (s[start] == s[end])
                    
                if dp[start][end] and (end - start + 1) > (lpsend - lpsstart + 1):
                    lpsstart = start
                    lpsend = end
                    
                start = start - 1
        return s[lpsstart:lpsend+1]
