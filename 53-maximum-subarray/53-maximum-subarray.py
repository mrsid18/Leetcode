class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        ans = -inf
        for n in nums:
            if res<=0:res=n
            else: res+=n
            ans = max(ans, res)
        
        return ans