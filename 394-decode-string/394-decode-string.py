class Solution:
    def decodeString(self, s: str) -> str:
        res = [""]
        k=1
        stack = []
        
        for i, c in enumerate(s):
            if c=="[":
                k=1
                idx=i-1
                temk=""
                while s[idx].isdigit(): 
                    temk+=s[idx]
                    idx-=1
                res.append("")
                if temk:
                    stack.append(int(temk[::-1]))
                else:
                    stack.append(int(k))
            elif c=="]":
                cur = res.pop()
                k = stack.pop()
                res[-1]+=k*cur
            elif s[i].isalpha():
                res[-1]+=c
        return res[-1]
                
                
            
                
                    
                
                