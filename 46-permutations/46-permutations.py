class Solution:
    def permute(self, nums):
        res = []
        
        def dfs(sub, ans):
            if len(ans)==len(nums): 
                res.append(ans.copy())
                return
            
            for i, n in enumerate(sub):
                ans.append(n)
                dfs(sub[0:i]+sub[i+1:], ans)
                ans.pop()
        
        dfs(nums, [])
        return res
            
                