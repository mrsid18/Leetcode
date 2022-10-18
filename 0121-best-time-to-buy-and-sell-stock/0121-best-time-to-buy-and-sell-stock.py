class Solution:
    def maxProfit(self, prices: List[int]):
        res = -inf
        buy = inf
        for p in prices:
            if p-buy<0:
                buy=p
            else:
                res = max(res, p-buy)
                
        return 0 if res==-inf else res
        