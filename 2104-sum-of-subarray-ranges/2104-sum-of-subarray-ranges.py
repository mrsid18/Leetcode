class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i, n in enumerate(nums):
            mini = maxi = n
            for j in range(i+1, len(nums)):
                maxi = max(nums[j],maxi)
                mini = min(nums[j], mini)
                res += maxi-mini
        
        return res