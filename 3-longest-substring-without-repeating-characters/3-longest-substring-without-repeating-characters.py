class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        res = 1
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]: break
                res = max(res, j-i+1)
                
        return res