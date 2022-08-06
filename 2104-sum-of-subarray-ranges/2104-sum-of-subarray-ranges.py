class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        res = 0
        
        for i in range(len(nums)):
            maxi = mini = nums[i]
            for j in range(i+1, len(nums)):
                maxi = max(maxi, nums[j])
                mini = min(mini, nums[j])
                res += maxi-mini
        
        return res