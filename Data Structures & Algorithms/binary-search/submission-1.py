class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) # initialize the variables
        # loop
        while l<r:
            # middle = distance between left and right of list, change position* 
            m = l + ((r - l) // 2)
            # nums[index] > target --> right move to middle
            if nums[m] > target:
                r = m
            # nums[index] < target --> left move to +1 
            elif nums[m] < target:
                l =m+1 
            #return index that value equals target
            else :
                return m
               
        # value not equal target --> return -1
        return -1