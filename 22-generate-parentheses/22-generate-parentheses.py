class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(ans, o, c):
            if o==n and c==n:
                res.append(ans)
                return
            if o<n:
                backtrack(ans+"(", o+1, c)
            if c<o:
                backtrack(ans+")", o, c+1)
            
        backtrack("",0, 0)
        
        return res