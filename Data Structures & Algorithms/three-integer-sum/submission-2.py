class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two point
        
       
        expected =0
        result =[]
        #sort nums to use two pointers 
        nums = sorted(nums)
        for i in range( len(nums) -2):
            #initial left and right position
            l = i+1
            r = len(nums)-1
        # loop through left less than right position
            while l < r:
                total = nums[l] + nums[i] + nums[r]
                #if total <0 --> move left position up
                if(total < expected):
                    l+=1
                #if total > 0 --> move right position down
                elif(total >expected):
                    r-=1
                #equal?--> check if it duplicates or not, duplicate triplets? --> remove that triplets
                else:
                    triplet=[nums[l], nums[i], nums[r]]
                    if(triplet not in result):
                        result.append(triplet)
                    #move positions after found the result
                    l+=1
                    r-=1
        return result