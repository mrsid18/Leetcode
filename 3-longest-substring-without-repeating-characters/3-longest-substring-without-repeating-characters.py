class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r = 0, 1
        maxL = 1
        while l < len(s)-1:
            r=l+1
            while r < len(s):
                if s[r] in s[l:r]:
                    # maxL = max(maxL, r-l)
                    break
                maxL = max(maxL, r-l+1)
                r+=1
            l+=1
        return maxL
        
        