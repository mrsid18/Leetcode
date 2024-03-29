"""
1, 2, 5 
1->1 coin
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            for c in coins:
                if i>=c: dp[i] = min(dp[i], 1+dp[i-c])
                else: break
        return dp[amount] if dp[amount]!=amount+1 else -1
            
            
            
        
        