class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = -inf
        for n in nums:
            s+=n
            res = max(res, s)
            if s<0: s=0
        
        return res
            