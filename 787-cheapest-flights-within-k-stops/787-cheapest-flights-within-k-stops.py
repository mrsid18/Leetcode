class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Bellman Ford Algorithm
        
        cost = [inf]*n
        cost[src] = 0
        
        for i in range(k+1):
            tmp = cost.copy()
            
            for s, d, c in flights:
                if cost[s]==inf:
                    continue
                if cost[s]+c<tmp[d]:
                    tmp[d] = cost[s]+c
            
            cost = tmp
            
        return -1 if cost[dst]==inf else cost[dst]