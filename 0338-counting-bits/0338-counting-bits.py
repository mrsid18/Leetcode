"""
the bruteforce way is to get the binary representation of each number and count number of 1's in it
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(n+1):
            res[i] = res[i//2]+i%2
        
        return res
        
        
            
            
        