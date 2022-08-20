class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        def dfs(i, arr):
            if i==len(digits): return arr
            
            tmp = []
            for c in dmap[digits[i]]:
                for combi in arr:
                    tmp.append(combi+c)
            
            return dfs(i+1, tmp)
        
        return dfs(0, [""]) if digits else []