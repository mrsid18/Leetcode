class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        s = 0
        for n in nums:
            if s>0: s+=n
            else: s = n
            
            res = max(res, s)
        
        return res