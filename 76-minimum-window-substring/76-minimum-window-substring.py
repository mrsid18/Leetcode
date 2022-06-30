class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        req = 0
        for c in t:
            if c in tmap: tmap[c]+=1
            else:
                req+=1
                tmap[c]=1
        
        smap = {}
        
        l, r = 0, 0
        
        resL, resR = 0, len(s)
        match = 0
        while r<len(s):
            smap[s[r]] = smap.get(s[r],0)+1
            
            if s[r] in tmap and smap[s[r]]==tmap[s[r]]: match+=1
                
            while req==match and l<=r:
                if r-l<resR-resL: resR, resL = r, l
                if s[l] in tmap and smap[s[l]]==tmap[s[l]]: match-=1
                smap[s[l]]-=1
                l+=1
            
            r+=1
        
        return s[resL:resR+1] if resR!=len(s) else ""
                
            