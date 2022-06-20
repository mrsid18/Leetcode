class Solution:
    def maxProfit(self, prices: List[int]):
        #buy low sell high
        res = 0
        
        min_price = prices[0]
        
        for p in prices:
            d = p - min_price
            if d<0: min_price = p
            res = max(res, d)
        
        return res
        