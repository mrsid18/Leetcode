class Solution:
    def minWindow(self, s: str, t: str) -> str:
        thash = {}
        shash = {}
        need, have = 0, 0
        l, r = 0,0
        resL, resR = 0, len(s)+1
        for i in range(len(t)):
            need += 0 if t[i] in thash else 1
            thash[t[i]] = thash.get(t[i],0) + 1
        while r<len(s):
            shash[s[r]] = shash.get(s[r],0) + 1
            
            if s[r] in thash and shash[s[r]]==thash[s[r]]: have+=1 
            while need==have and l<=r:
                if resR-resL>=r-l: resL, resR = l, r
                if s[l] in thash and shash[s[l]] == thash[s[l]]: have -= 1
                shash[s[l]]-=1 if shash[s[l]] else 0
                l+=1
            
            r+=1
        return "" if resR == len(s)+1 else s[resL:resR+1]