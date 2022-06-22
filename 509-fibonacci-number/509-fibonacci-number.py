class Solution:
    def fib(self, n: int) -> int:
        if not n: return 0
        l, r = 0, 1
        
        for i in range(1,n):
            l, r = r, l+r
        
        return r