class Solution:
    def isValid(self, s: str) -> bool:
        #today learning stack 
        #save the pairs 
        pairs ={
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        # intialize stack
        stack =[]
        # loop
        for c in s:
            # c have the open --> save into stack
            if c in '{[(':
                stack.append(c)
            else:
                # stack empty -->false
                if not stack:
                    return False
                #get the last array of stack to compare
                top = stack.pop()
                # not equal --> return false
                if top != pairs[c]:
                    return False
        return stack ==[] # return True if stack is empty


