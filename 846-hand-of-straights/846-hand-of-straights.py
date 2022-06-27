class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False
        
        hmap = {}
        
        for n in hand:
            hmap[n] = hmap.get(n, 0)+1
        
        minHeap =list(hmap.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            s = minHeap[0]
            if hmap[s]==0:
                heapq.heappop(minHeap)
                continue
            hmap[s] -=1
            for i in range(1,groupSize):
                if s+i in hmap and hmap[s+i]: hmap[s+i]-=1
                else: return False
        
        return True