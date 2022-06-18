class MedianFinder:

    def __init__(self):
        self.sh = []
        self.lh = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.sh, -1*num)
        
        if self.lh and num>self.lh[0]:
            heapq.heappush(self.lh, num)
            heapq.heappop(self.sh)
            
        if len(self.sh)>len(self.lh)+1:
            ele = heapq.heappop(self.sh)
            heapq.heappush(self.lh, -1*ele)
        if len(self.lh)>len(self.sh)+1:
            ele = heapq.heappop(self.lh)
            heapq.heappush(self.sh, -1*ele)
        
    def findMedian(self) -> float:
        if len(self.sh)>len(self.lh):
            return -1*self.sh[0]
        elif len(self.lh)>len(self.sh):
            return self.lh[0]
        else:
            return (-1*self.sh[0] +self.lh[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()