class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        /*
        if(nums.length == 1)
            return false;
        
        int res = nums[0];
        int count = 1;
        for(int i=1; i<nums.length; i++) {
            res += nums[i];
            int val = res;
            count+=1;
            int temp = count;
            if(res%k == 0)
                return true;
            int j = 0;
            while(temp > 2) {
                val -= nums[j];
                if(val%k == 0)
                    return true;
                j++;
                temp--;
            }
        }
        return false;
        */
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        for(int i=1; i<n; i++) {
            dp[i] = nums[i] + dp[i-1];
            if(nums[i] == 0 && nums[i-1] == 0)
                return true;
            if(dp[i]%k == 0)
                return true;
        }
        if(dp[n-1] < k) return false;
        
        for(int i=0; i<n-2; i++) {
            for(int j=i+2; j<n; j++) {
                if((dp[j]-dp[i])%k == 0)
                    return true;
            }
        }
        return false;
    }
}
