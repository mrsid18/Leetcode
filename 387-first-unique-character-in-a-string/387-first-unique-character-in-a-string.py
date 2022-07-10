class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = Counter(s)
        
        for idx, c in enumerate(s):
            if hmap[c]==1: return idx
        
        return -1