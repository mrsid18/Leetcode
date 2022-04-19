class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0, 1:1}
        
        def recur(n):
            if n in cache:
                return cache[n]
            cache[n] = recur(n-1) + recur(n-2)
            return cache[n]
        
        return recur(n)