class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}
        
        def cs(n):
            if n in cache:
                return cache[n]
            
            cache[n] = cs(n-1)+cs(n-2)
            return cache[n]
        
        return cs(n)