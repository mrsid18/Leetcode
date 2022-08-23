class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = {}
        
        for i in range(len(s)):
            last[s[i]] = i
        
        l, r = 0, len(s)-1
        resL, resR = 0, 0
        
        while resL<=resR and resR<len(s):
            l = resL
            while l<=resR:
                resR = max(resR, last[s[l]])
                l+=1
            res.append(resR-resL+1)
            resR+=1
            resL = resR
            
        return res
            
                
            
            