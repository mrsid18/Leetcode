import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = re.sub('[^a-zA-Z0-9]', "", s).lower()
        return s[::-1]==s
        l = len(s)
        for i in range(l//2):
            if ord(s[i]) - ord(s[l-i-1]) != 0:
                return False
        return True