class Solution:
    def largestVariance(self, s: str) -> int:
        charlist = defaultdict(list)
        
        for i,c in enumerate(s):
            charlist[c].append(i)
        
        res = 0
        
        chars = charlist.keys()
        for target in chars:
            for char in chars:
                if target != char:
                    i = j = 0
                    charcount = targetcount = 0
                    while i<len(charlist[target]) and j<len(charlist[char]):
                        if charlist[char][j] < charlist[target][i]:
                            charcount +=1
                            j+=1
                            
                            if charcount>targetcount:
                                charcount = 0
                                targetcount = 0
                        else:
                            targetcount +=1
                            i+=1
                            if targetcount == charcount:
                                charcount = 0
                                targetcount = 0
                                
                            res = max(res, targetcount-max(charcount, 1))
                        
                    if i<len(charlist[target]):
                        res = max(res, targetcount-max(charcount,1)+len(charlist[target])-i)
                            
        return res
                                
                            