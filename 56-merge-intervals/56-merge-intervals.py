class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i=1
        
        while i<len(intervals):
            prev, cur = intervals[i-1], intervals[i]
            if cur[0]<=prev[1]:
                prev[1] = max(prev[1],cur[1])
                del intervals[i]
            else:
                i+=1
        
        return intervals
            
            