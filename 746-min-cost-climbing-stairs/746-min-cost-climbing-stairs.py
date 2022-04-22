class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up solution
       
        jc = [0,0]
        for n in cost[::-1]:
            temp = min(n+jc[0], n+jc[1])
            jc[1] = jc[0]
            jc[0] = temp
            
        return min(jc)
            
        
            
            
        