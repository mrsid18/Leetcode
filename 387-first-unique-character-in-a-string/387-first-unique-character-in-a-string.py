class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}
        
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        
        for key, value in hmap.items():
            if value==1:return s.index(key)
        
        return -1