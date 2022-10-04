class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = defaultdict(int)
        
        res = 0
        
        for c in s:
            hmap[c]+=1
        
        for key, val in hmap.items():
            if val==1: return s.index(key)
        
        return -1