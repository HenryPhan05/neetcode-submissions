class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #initialize the value output
        maxArea = 0
        height = 0 
        width =0
        #initialize two cursor
        l =0 
        r= len(heights) -1
        #looping 
        while l < r: 
     
            # width is the distance of the container
            width = r - l 
            #height is the highest to contain most water
            height = min(heights[l], heights[r])
            area = width * height
            # get the max area
            if area >= maxArea:
                maxArea = area
            # after progress, move both left and right
                   # condition , if value in left less than right --> move left , otherwise move right, if both equal, not change the position
            if(heights[l] < heights[r]):
                l+=1
            elif(heights[l] > heights[r]):
                r-=1
            else:
                l+=1
                r-=1
        return maxArea