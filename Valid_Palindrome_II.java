class Solution {
    public boolean validPalindrome(String s) {
        int low = 0, high = s.length()-1;
        
        while(low < high) {
            if(s.charAt(low) == s.charAt(high)) {
                low++;
                high--;
            } else {
                if(isPalindrome(s, low+1, high))
                    return true;
                if(isPalindrome(s, low, high-1))
                    return true;
                return false;
            }
        }
        return true;
    }
    
    public boolean isPalindrome(String s, int l, int h) {
        while(l < h) {
            if(s.charAt(l) != s.charAt(h))
                return false;
            l++;
            h--;
        }
        return true;
    }
}
