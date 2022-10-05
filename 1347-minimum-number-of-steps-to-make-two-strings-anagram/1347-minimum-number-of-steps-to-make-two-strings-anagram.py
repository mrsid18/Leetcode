class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scount = Counter(s)
        tcount = Counter(t)
        res = 0
        for key, val in scount.items():
            if val-tcount[key]>0: res+=val-tcount[key]
        
        return res