class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        
        for n in numSet:
            if n-1 not in numSet:
                length = 0
                while n in numSet:
                    length+=1
                    n+=1
                longest = max(longest, length)
            
        return longest
                