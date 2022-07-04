class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(tmp, cur, end):
            if cur==end:
                ans.append(tmp[:])
            else:
                tmp.append(nums[cur])
                dfs(tmp, cur+1, end)
                tmp.pop()
                dfs(tmp, cur+1, end)
        
        ans = []
        dfs([], 0, len(nums))
        return ans