class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        con = defaultdict(list)
        count = [0]*n
        for r1,r2 in roads:
            con[r1].append(r2)
            con[r2].append(r1)
            count[r1]+=1
            count[r2]+=1
        
        bucket = [[] for _ in range(n)]
        
        for idx, c in enumerate(count):
            bucket[c].append(idx)
        
        s = sorted(list(set(count)))
        check = bucket[s[-1]]
        if len(check)<2:
            check.extend(bucket[s[-2]])
        
        res = -inf
        for i, r1 in enumerate(check):
            for j in range(i+1, len(check)):
                r2 = check[j]
                if r1 in con[r2]:
                    res = max(res, count[r1]+count[r2]-1)
                else:
                    res = max(res, count[r1]+count[r2])
            
        return res