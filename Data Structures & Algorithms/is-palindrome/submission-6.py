class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = ""
        left = ""
        arr = ""
    
        for c in s :
            if c.isalnum():
               arr +=c.lower()
        
        for i in range(int(len(arr) /2 )):
            left = arr[i]
            right = arr[len(arr) -i - 1]
            if(left != right):
                return False
        return True
        