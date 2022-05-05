class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        maxL = 0
        charSet = set()
        while r<len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxL = max(maxL, r-l+1)
            r+=1
            
        return maxL
        
        