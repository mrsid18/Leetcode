class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        l, r = 0, 0
        
        for i in range(len(nums)-1):
            l, r = r, max(nums[i]+l, r)
        
        l2, r2 = 0, 0
        
        for i in range(1, len(nums)):
            l2, r2 = r2, max(nums[i]+l2, r2)
        
        return max(r, r2)