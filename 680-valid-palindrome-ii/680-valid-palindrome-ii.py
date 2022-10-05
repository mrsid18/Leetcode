class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(s, once):
            l, r = 0, len(s)-1
            
            while l<r:
                if s[l]!=s[r]:
                    if once: return False
                    return check(s[l:r], True) or check(s[l+1:r+1], True)
                else:
                    l+=1
                    r-=1
                
            return True
        
        return check(s, False)