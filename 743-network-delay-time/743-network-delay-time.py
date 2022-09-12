class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        
        for s, d, t in times:
            adj[s].append([t, d])
        
        visited = set()
        cost = [inf]*(n+1)
        minH = [[0,k]]
        
        while len(visited)<n and minH:
            tmp = cost.copy()
            p, i = heapq.heappop(minH)
            
            if i in visited: continue
            
            cost[i] = p
            visited.add(i)
            
            for c,d in adj[i]:
                if d not in visited: heapq.heappush(minH, [c+p, d])
                
        cost.pop(0)
        
        return -1 if inf in cost else max(cost) 
            
            
                
                
            