class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # intialize left and right for binary search
        l, r = 1, max(piles) 
        result = 0
        # loop through
        while l<=r:
            # speed eating
            k  = (l+r)//2
            hours = 0 
            for pile in piles :
                # time to eat , round up the hours
                hours +=math.ceil(pile /k)
            # find the min speed to eat at all bananas at those totalHours
            if hours <= h:
                result = k
                r = k -1
            else:
                l = k+1
        return result
    #revise this problem again, because it's so hard to solve it
