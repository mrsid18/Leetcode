class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        rob1, rob2 = 0, 0
        
        for n in nums[:-1]:
            rob1, rob2 = rob2, max(n+rob1, rob2)
        
        r1 = max(rob1, rob2)
        
        rob1, rob2 = 0, 0
        for n in nums[1:]:
            rob1, rob2 = rob2, max(n+rob1, rob2)
        
        r2 = max(rob1, rob2)
        
        return max(r1, r2)
            