class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            b = target-num
            if b in hmap: return [hmap[b], i]
            hmap[num] = i
        