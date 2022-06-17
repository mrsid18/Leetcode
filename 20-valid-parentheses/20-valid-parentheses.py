from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        
        stack = []
        
        for c in s:
            if c in brackets and stack:
                if brackets[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        if stack: return False
        
        return True
                
        
        