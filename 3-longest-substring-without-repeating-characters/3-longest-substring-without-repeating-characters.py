class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #because longest substring = consecutive, we can use sliding window method
        if not s:
            return 0
        l, r = 0,1
        maxOut = 1
        while r<len(s):
            while l<r and s[r] in s[l:r]:
                l+=1
            maxOut = max(maxOut, r-l+1)
            print(maxOut)
            r+=1
        
        return maxOut
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = 0
#         maxL = 0
#         charSet = set()
#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l+=1
#             charSet.add(s[r])
#             maxL = max(maxL, r-l+1)
#             r+=1
            
#         return maxL
        
        