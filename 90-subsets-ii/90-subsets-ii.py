class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, sub):
            if i==len(nums):
                if sub not in res: res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i+1, sub)
            
            sub.pop()
            dfs(i+1, sub)
        
        nums.sort()
        dfs(0, [])
        return res