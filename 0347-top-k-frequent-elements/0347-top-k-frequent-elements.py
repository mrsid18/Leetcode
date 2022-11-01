class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        
        h = []
        
        for num, count in c.items():
            h.append((-count, num))
            
        heapq.heapify(h)
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(h)[1])
            
        return res