class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res+=1
            n = n & (n-1)
        
        return res
        
        
        res = 0
        while n:
            res += n%2
            n = n >> 1
        
        return res
        
        