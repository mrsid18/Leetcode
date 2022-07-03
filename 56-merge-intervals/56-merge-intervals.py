class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # just the last interval
        
        res = []
        intervals.sort(key=lambda x:x[0])
        for i in intervals:
            if not res: res.append(i)
            else:
                pl, pr = res[-1][0], res[-1][1]
                l, r = i[0],i[1]
                if pl<=l<=pr:
                    if r>pr: res[-1][1] = r
                else:
                    res.append(i)
        
        return res