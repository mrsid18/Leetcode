class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = []
        print(intervals)
        for i in range(len(intervals)):
            if res and intervals[i][0]<=res[-1][1]:
                if res[-1][1]<intervals[i][1]: res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        
        return res