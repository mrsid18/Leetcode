class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        if len(s)<=1: return len(s)
        res = 1
        l, r = 0, 1
        while r<len(s):
            while s[r] in s[l:r]:
                l+=1
            res = max(res, r-l+1)
            r+=1
        
        return res
        
        #Brute force method O(n**2)
        if not s: return 0
        res = 1
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]: break
                res = max(res, j-i+1)
                
        return res