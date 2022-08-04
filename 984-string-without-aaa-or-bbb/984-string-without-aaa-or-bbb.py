class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        def dfs(A, B, a='a', b='b', res=""):
            
            if B>A: return dfs(B, A, 'b', 'a')
            
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
        
        return dfs(a, b)
            
                
                
                    
                
            