class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(tmp, start, end):
            if start==end and tmp not in ans:
                ans.append(tmp[:])
            else:
                for idx in range(start, end):
                    tmp.append(nums[idx])
                    dfs(tmp, idx+1, end)
                    tmp.pop()
                    dfs(tmp, idx+1, end)
        
        ans = []
        dfs([], 0, len(nums))
        return ans