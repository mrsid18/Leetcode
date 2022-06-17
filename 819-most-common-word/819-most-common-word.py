class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.sub('\W', ' ', paragraph)
        words = p.split( )
        hmap = {}
        res = ""
        m = 0
        for word in words:
            word = word.lower()
            hmap[word] = hmap.get(word, 0) + 1
           
        
        for w,freq in hmap.items():
            if freq>m and w not in banned:
                m = freq
                res = w
        
        return res