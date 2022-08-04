class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        a, b = 'a', 'b'
        if B>A:
            A, B = B, A
            a, b = b, a
        
        res = ""
        while A>0:
            res += a
            A-=1
            if A>B:
                res+=a
                A-=1
            if B>0:
                res+=b
                B-=1
                
        return res
            
                
                
                    
                
            