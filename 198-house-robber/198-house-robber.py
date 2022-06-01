class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        
        for n in nums:
            r1,r2 = r2, max(n+r1, r2)
        
        return max(r1, r2)