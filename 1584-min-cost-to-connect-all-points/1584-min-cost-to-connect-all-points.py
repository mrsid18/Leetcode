class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #graph theory problem
        #Prim's algorithm
        
        adj = defaultdict(list)
        N = len(points)
        
        visited = set()
        
        for i in range(N):
            x, y = points[i]
            for j in range(i+1, N):
                x1, y1 = points[j]
                cost = abs(x-x1) + abs(y-y1)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
                
        #Prim's algorithm
        
        minH = [[0, 0]]
        res = 0
        
        while len(visited)<N:
            cost, node = heapq.heappop(minH)
            
            if node in visited:
                continue
            
            visited.add(node)
            res += cost
            
            for nei in adj[node]:
                heapq.heappush(minH, nei)
            
        return res
            
                