class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, sub):
            if i==len(nums) or sum(sub)>target: return
            if sum(sub)==target:
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i, sub)
            
            sub.pop()
            dfs(i+1, sub)
            
        dfs(0, [])
        return res