class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[] # save the time that car meet together
        #convert to tuple(pos, spd)
        cars = sorted(zip(position, speed), reverse= True)
        #loop through cars
        for pos, spd in cars:
            
            time = (target-pos)/spd
            # if stack is empty , not carFleet --> append
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)