class Solution:
    def longestPalindrome(self, s: str) -> str:
        resl, resr, reslen = 0, 0, 0
        
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > reslen:
                    reslen = r-l+1
                    resl, resr = l, r
                l-=1
                r+=1
            
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > reslen:
                    reslen = r-l+1
                    resl, resr = l, r
                l-=1
                r+=1
            
        return s[resl:resr+1]