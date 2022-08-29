class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = ["+","-","/","*"]
        stack = []
        
        for t in tokens:
            num = t
            if t in opr:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if t=="*":
                    num = n1*n2
                elif t=="+":
                    num = n1+n2
                elif t=="/":
                    num = int(float(n1)/n2)
                else:
                    num = n1-n2
            stack.append(num)
        
        return stack[-1]
                