"""
make a counter object of all the strings and map it to the string
iterate over each strings in strs and check if any of the strs have same counter object
if same -> delete it and add it to array
now iterate through the second and check again
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
            
        return res.values()