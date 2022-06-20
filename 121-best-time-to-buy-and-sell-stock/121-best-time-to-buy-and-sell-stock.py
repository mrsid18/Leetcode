class Solution:
    def maxProfit(self, prices: List[int]):
        #buy low sell high
        res = 0
        
        l, r = 0, 1
        
        while r<len(prices):
            if prices[r]-prices[l]<0:
                l = r
            
            res = max(res, prices[r]-prices[l])
            r+=1
        
        return res
        