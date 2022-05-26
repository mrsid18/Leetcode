class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        charset1,charset2 = {}, {}
        
        for i in range(len(s1)):
            charset1[s1[i]] = 1 + charset1.get(s1[i], 0)
        
        for i in range(len(s1)-1):
            charset2[s2[i]] = 1 + charset2.get(s2[i], 0)
        
        l, r=0, len(s1)-1
        
        while r<len(s2):
            charset2[s2[r]] = 1+charset2.get(s2[r], 0)
            if charset2==charset1:
                return True
            charset2[s2[l]] -= 1
            if not charset2[s2[l]]: del charset2[s2[l]]
            l+=1
            r+=1
        
        return False
        
        
        
        