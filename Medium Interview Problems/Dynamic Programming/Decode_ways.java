class Solution {
    public int numDecodings(String s) {
        // char[] digit = s.toCharArray();
        return helper(s, s.length());
    }
    
    public int helper(String s, int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        
        for(int i=1; i<=n; i++) {
            if(s.charAt(i-1) == '0')
                dp[i] = 0;
            else
                dp[i] = dp[i-1];
            if(i-2 >= 0) {
                int dig = Integer.parseInt(s.substring(i-2, i));
                if(dig >= 0 && dig <= 26 && dig>9)
                    dp[i] += dp[i-2];
            }
        }
        
        return dp[n];
    }
}
