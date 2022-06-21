class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # dp = [False]*(len(s)+1)
        # dp[len(s)] = True
        words = [[] for _ in range(len(s)+1)]
        words[len(s)].append("")
        res = []

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    for word in words[i+len(w)]:
                        words[i].append(w+" "+word)
        
        return [w.rstrip() for w in words[0]]
                    
                    
                