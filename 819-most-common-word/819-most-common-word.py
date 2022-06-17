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
            if hmap[word]>m and word not in banned:
                m = hmap[word]
                res = word
            
        return res