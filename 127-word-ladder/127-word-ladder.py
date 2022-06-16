class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        visited = set()
        wordList.append(beginWord)
        nei = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                nei[pattern].append(word)
        
        res = 1
        q = deque([beginWord])
        
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word==endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for w in nei[pattern]:
                        if w not in visited:
                            visited.add(w)
                            q.append(w)
            res+=1

        return 0
                
        
        