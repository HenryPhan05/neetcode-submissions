class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0] * len(temperatures)
        stack =[] #pair [temp, index]
        for i, t in enumerate(temperatures): # get the index and temperature in arr
            #why temp compares with stack[-1][0] , not stack[-1][-1] or stack[-1]?
            #--> cuz stack contains two values in one index, first value is temp and other one is index, [[75,1], [30,2]]
            # why it need to contain like that? 
            #--> cuz it not only compares the temperatures each day, but also it has to save the distance from the day has higher temperature than prev day into `result`
            while stack and t > stack[-1][0]: # while stack is not empty temp in ar greater than temp in top of stack 
                stackT, stackInd= stack.pop() # pop the temperature and index
                result[stackInd]= (i - stackInd) # save distance from day has higher temperature than prev
            stack.append([t,i]) # append temp and index into stack
        return result
    #do again to recall