class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(list(set(nums)))
        res = 1
        cs = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                cs+=1
            else:
                cs=1
            res = max(res, cs)
        
        return res