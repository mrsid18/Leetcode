class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, sub):
            if i==len(nums):
                res.append(sub.copy())
                return
            
            # sub.append(nums[i])
            dfs(i+1, sub+[nums[i]])
            
            # sub.pop()
            dfs(i+1, sub)
            
        dfs(0, [])
        
        return res
        
            
            
    