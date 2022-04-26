from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        paran = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        
        stack = []
        
        for c in s:
            if c in paran and stack:
                if paran[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        if len(stack):
            return False
        return True
        