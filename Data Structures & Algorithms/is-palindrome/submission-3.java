class Solution {
    public boolean isPalindrome(String s) {
        // this exercise check the forward and backward is same or not
        // idea: for loop then check both left and right position in one array
        char[] chars = s.toCharArray();
        StringBuilder result = new StringBuilder();
        // remove numbers and symbols and convert to lowercase
        for(char c: chars) { 
			if(Character.isLetterOrDigit(c)) {
				result.append(Character.toLowerCase(c));
			}
        }
            chars = result.toString().toCharArray();
            int left = 0;
            int right = chars.length-1;
            while(left<=right) {
				if(chars[left] != chars[right]) {
					return false;
                }
                left++;
                right--;
			}
          return true;
		}
   
    }

