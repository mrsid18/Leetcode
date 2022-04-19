class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def recur(n):
            if n<=1:
                return n
            if n in cache:
                return cache[n]
            cache[n] = recur(n-1) + recur(n-2)
            return cache[n]
        
        return recur(n)