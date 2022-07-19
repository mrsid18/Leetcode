class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        disjoint = []
        for i in range(0, len(intervals)):
            if disjoint and intervals[i][0]<disjoint[-1][1]:
                res+=1
                if intervals[i][1]<disjoint[-1][1]:
                    disjoint.pop()
                    disjoint.append(intervals[i])
            else:
                disjoint.append(intervals[i])
        
        print(intervals, disjoint)
        return res