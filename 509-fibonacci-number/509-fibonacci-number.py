class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0, 1:1}
        
        def recur(n):
            if n in cache:
                return cache[n]
            ans = recur(n-1) + recur(n-2)
            cache[n] = ans
            return ans
        
        return recur(n)