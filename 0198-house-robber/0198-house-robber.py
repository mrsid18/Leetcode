class Solution:
    def rob(self, nums: List[int]) -> int:
        l, r = 0, 0
        for n in nums:
            l, r = r, max(l+n, r)
        return r