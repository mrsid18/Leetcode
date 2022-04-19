class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0:0, 1:1, 2:1}
        
        def tri(n):
            if n in cache:
                return cache[n]
            ans = tri(n-1)+tri(n-2)+tri(n-3)
            cache[n]=ans
            return ans
        
        return tri(n)
            