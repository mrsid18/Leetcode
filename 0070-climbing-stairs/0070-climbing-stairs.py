"""
1 stair -> 1 way
2 -> 2 ways
3 -> (2 stairs + 1) + (1 stair + 1)
4 -> (3 stairs + 1) + (2 stairs + 1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 1, 1
        for i in range(2, n+1):
            l, r = r, l+r
        return r