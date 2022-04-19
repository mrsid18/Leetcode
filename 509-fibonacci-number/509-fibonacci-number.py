class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def recur(n):
            if n<=1:
                return n
            if n in cache:
                return cache[n]
            ans = recur(n-1) + recur(n-2)
            cache[n] = ans
            return ans
        
        return recur(n)