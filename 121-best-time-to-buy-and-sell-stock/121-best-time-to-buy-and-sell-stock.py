class Solution:
    def maxProfit(self, prices: List[int]):
        #buy low sell high
        res = 0
        
        l, r = 0, 1
        
        while r<len(prices):
            d = prices[r]-prices[l]
            if d<0: l = r
            res = max(res, d)
            r+=1
        
        return res
        