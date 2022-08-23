class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        l, r = 0, len(s)-1
        resL, resR = 0, 0
        
        while resL<=resR and resR<len(s):
            l = resL
            while l<=resR:
                while r>=resR and s[r]!=s[l]:
                    r-=1
                resR = max(resR, r)
                l+=1
                r=len(s)-1
            res.append(resR-resL+1)
            resR+=1
            resL = resR
            
        return res
            
                
            
            