class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        newStack= []
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                b = int(newStack.pop())
                a = int(newStack.pop())
                match tokens[i]:
                    case '+':
                        newStack.append(a+b)
                    
                    case '-':
                        newStack.append(a-b)
                      
                    case '*':
                        newStack.append(a*b)
                       
                    case '/':
                        newStack.append(int(a/b))
                   
            else: 
                newStack.append(int(tokens[i]))
            
        return newStack[0]
                

            