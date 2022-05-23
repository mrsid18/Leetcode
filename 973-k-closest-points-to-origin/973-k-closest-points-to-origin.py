class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #find the sum of squares of the points
        
        minHeap = []
        
        for x,y in points:
            minHeap.append([x**2+y**2, x, y])
        
        heapq.heapify(minHeap)
        
        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res
                