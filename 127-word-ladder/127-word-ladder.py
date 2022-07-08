class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        nei = defaultdict(list)
        
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                nei[pattern].append(word)
                
        visited = set()
        
        q = deque([beginWord])
        
        res = 1
        while q:
            n = len(q)
            for i in range(n):
                word = q.popleft()
                
                if word==endWord: return res
                
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for match in nei[pattern]:
                        if match not in visited:
                            visited.add(match)
                            q.append(match)
            
            res+=1
        
        return 0
        
        
        
        