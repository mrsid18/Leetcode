import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        y = re.sub('[^a-zA-Z0-9]', "", s).lower()
        m = len(y)//2
        l = len(y)
        for i in range(m):
            if ord(y[i]) - ord(y[l-i-1]) != 0:
                return False
        return True