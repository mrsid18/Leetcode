class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -inf
        tmax, tmin = 1, 1
        
        for n in nums:
            if n==0:
                tmax, tmin = 1, 1
            
            tmp = tmax*n
            tmax = max(n*tmax, n*tmin, n)
            tmin = min(tmp, n*tmin, n)
            res = max(tmax, res)
        
        return res
            
            