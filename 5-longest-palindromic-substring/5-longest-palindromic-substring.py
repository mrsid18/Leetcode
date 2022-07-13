class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        
        for i in range(len(s)):
            l, r = i, i #for odd
            
            while l>-1 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1])>len(res): res = s[l:r+1]
                l-=1
                r+=1
            
            l, r = i, i+1 #for even
            while l>-1 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1])>len(res): res = s[l:r+1]
                l-=1
                r+=1
        
        return res