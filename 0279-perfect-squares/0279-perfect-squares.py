"""
One way of thinking can be like 
1. Make an array of squares till n//2
1 -> 1
2->1+1
3->2+1
4->3+1, 4
5->4+1
6->dp[5]+1
8->dp[7]+dp[1], dp[4]+dp[4]
9->dp[4]+dp[5], 1
12->dp[11]+1, 4

"""



class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]