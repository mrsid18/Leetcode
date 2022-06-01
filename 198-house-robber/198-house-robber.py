class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums)==2:
        #     return max(nums)
        cache = {0:nums[0], -1:0}
        def res(n):
            if n in cache:
                return cache[n]
            cache[n] = max(nums[n]+res(n-2), res(n-1))
            return cache[n]
        
        return res(len(nums)-1)
    
    
        