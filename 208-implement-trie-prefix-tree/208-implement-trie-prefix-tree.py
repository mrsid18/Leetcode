class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True
        
    
    def search(self, word):
        cur = self.root
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False
        return cur.isWord
    
    
    def startsWith(self, word):
        cur = self.root
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False
        return True
        
    