class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(tmp, start, end):
            ans.append(tmp[:])
            for i in range(start, end):
                if i>start and nums[i]==nums[i-1]: continue
                tmp.append(nums[i])
                dfs(tmp, i+1, end)
                tmp.pop()
                
        ans = []
        nums.sort()
        dfs([], 0, len(nums))
        return ans