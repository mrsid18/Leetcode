class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False
        
        hmap = defaultdict(lambda: 0)
        
        for n in hand:
            hmap[n]+=1
        
        heap = list(hmap.keys())
        heapq.heapify(heap)
        
        while heap:
            f = heap[0]
            if hmap[f]<=0:
                heapq.heappop(heap)
                continue
            
            hmap[f]-=1
            
            for i in range(1,groupSize):
                if hmap[f+i]>0:
                    hmap[f+i]-=1
                else:
                    return False
        
        return True
