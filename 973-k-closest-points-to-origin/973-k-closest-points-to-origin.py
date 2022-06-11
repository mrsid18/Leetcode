class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for p in points:
            p.insert(0,p[0]**2+p[1]**2)
        
        heapq.heapify(points)
        res = []
        for _ in range(k):
            x,y,z = heapq.heappop(points)
            res.append([y,z])
        
        return res