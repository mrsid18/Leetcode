class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                l = 0
                while num+1 in nums:
                    l+=1
                    num = num+1
                res = max(l+1, res)
            
        return res