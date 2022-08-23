class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = -inf
        for n in nums:
            if s<0: s=0
            s+=n
            res = max(res,s)
        return res