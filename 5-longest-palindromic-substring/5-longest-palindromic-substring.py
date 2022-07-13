class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resL, resR = 0, 0
        
        for i in range(len(s)):
            l, r = i, i #for odd
            
            while l>-1 and r<len(s) and s[l]==s[r]:
                if r-l>resR-resL: resL, resR = l, r
                l-=1
                r+=1
            
            l, r = i, i+1 #for even
            while l>-1 and r<len(s) and s[l]==s[r]:
                if r-l>resR-resL: resL, resR = l, r
                l-=1
                r+=1
        
        return s[resL:resR+1]