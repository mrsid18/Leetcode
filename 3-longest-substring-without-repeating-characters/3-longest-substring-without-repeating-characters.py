class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r = 0, 1
        maxL = 1
        length = len(s)
        while l < length-1 and maxL != length:
            r=l+1
            while r < length:
                if s[r] in s[l:r]:
                    break
                maxL = max(maxL, r-l+1)
                r+=1
            l+=1
        return maxL
        
        