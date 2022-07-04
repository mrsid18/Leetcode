class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(tmp, start, end):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                dfs(tmp, i+1, end)
                tmp.pop()
        ans = []
        dfs([], 0, len(nums))
        return ans