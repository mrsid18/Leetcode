class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = [0]*26
        for c in s:
            hmap[ord(c)-ord('a')]+=1
        
        for idx, c in enumerate(s):
            if hmap[ord(c)-ord('a')]==1: return idx
        
        return -1