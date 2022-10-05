"""
First sort the intervals according to start times. 
Start iterating through the intervals, and the intervals once I find a intersection, remove the largest interval -> (end - start) 
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        
        res = 0
        
        resInt = intervals[0]
        
        for i in range(1, len(intervals)):
            prev_start, prev_end = resInt
            start, end = intervals[i]
            if start in range(prev_start, prev_end):
                resInt[1] = min(prev_end, end)
                res+=1
            else:
                resInt = intervals[i]
                
        return res