class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = math.prod(nums)
        
        if p>0: return 1
        if not p: return 0
        if p<0: return -1