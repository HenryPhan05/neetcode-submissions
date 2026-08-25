class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #using set to check if it duplicate, O(n) 
        '''
        so this will run 1 loop, if it contains duplicate value --> return True, 
        else this number will be added into set 
        return False if value unique
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        