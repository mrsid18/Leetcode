class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            p = prod(nums)
            return [p//x for x in nums]
        
        res = [0]*len(nums)
        zero = nums.index(0)
        res[zero] = prod(nums[:zero]) * prod(nums[zero+1:])
        
        return res
        
        
        
        
            