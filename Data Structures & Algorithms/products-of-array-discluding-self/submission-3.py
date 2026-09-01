class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I tried to optimize the complexity, at the last one I did the space complexity is O(n) , so i tried to get solution with space complexity is O(1)
        #initialize the variables , 
        result =[1] * len(nums) 
        prefix =1
        postfix = 1
        # go loop and mutiples values of left 
        for i in range(len(nums)):
            result[i] = prefix
            prefix *=nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            result[i] *=postfix
            postfix *= nums[i]
            
        return result


        