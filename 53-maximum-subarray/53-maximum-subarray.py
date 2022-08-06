class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = -inf
        for num in nums:
            s += num
            res = max(s,res)
            if s<0: s = 0
        
        return res