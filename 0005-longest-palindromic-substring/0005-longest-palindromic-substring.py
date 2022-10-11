class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resL, resR = 0, 0
        
        for i in range(len(s)):
            #check for odd
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l>resR-resL: resR, resL = r, l
                l-=1
                r+=1
                
            
            
            #check for even
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l>resR-resL: resR, resL = r, l
                l-=1
                r+=1
                
        
        return s[resL:resR+1]
        