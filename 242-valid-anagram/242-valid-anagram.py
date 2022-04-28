class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        for c in s:
            if c in t:
                idx = t.index(c)
                t = t[:idx] + t[idx+1:]
        
        if len(t):
            return False
        return True
#         inpHash = {}
#         for c in s:
#             inpHash[c] = inpHash.get(c, 0) + 1
            
#         for c in t:
#             if inpHash.get(c, 0) < 1:
#                 return False
#             inpHash[c] -= 1
#         return True

        