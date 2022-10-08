class Solution {
    public int majorityElement(int[] nums) {
        
        /*
        int[] arr = new int[50001];
        for(int i=0; i<nums.length; i++)
            arr[nums[i]]++;
        
        for(int i=0; i<50001; i++) {
            if(arr[i] > (nums.length/2))
                return i;
        }
        return -1;
        */
        
        int maj = majority(nums);
        if (isMajor(maj, nums))
            return maj;
        else
            return -1;
    }
    
    public int majority(int[] nums) {
        int maj = 0, count = 1;
        for(int i=1; i<nums.length; i++) {
            if (nums[maj] == nums[i])
                count++;
            else
                count--;
            if(count == 0) {
                maj = i;
                count = 1;
            }
        }
        return nums[maj];
    }
    
    public boolean isMajor(int num, int[] nums) {
        int count = 0;
        for(int i=0; i<nums.length; i++) {
            if (nums[i] == num)
                count++;
        }
        if(count > nums.length/2)
            return true;
        return false;
    }
}
