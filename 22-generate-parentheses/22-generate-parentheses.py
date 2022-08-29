class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(ans, o, c):
            if o==n and c==n:
                res.append(ans)
                return
            if o<n:
                dfs(ans+"(", o+1, c)
            if c<o:
                dfs(ans+")", o, c+1)
            
        dfs("",0, 0)
        
        return res
            
            