class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        
        def tri(n):
            if n<=2:
                return 1 if n else 0
            if n in cache:
                return cache[n]
            ans = tri(n-1)+tri(n-2)+tri(n-3)
            cache[n]=ans
            return ans
        
        return tri(n)
            