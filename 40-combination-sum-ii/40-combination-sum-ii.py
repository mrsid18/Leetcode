class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        subsets = []
        candidates.sort()
        length = len(candidates)
        def dfs(i, add):
            if i==length or add>=target:
                if add==target: res.append(subsets[:])
                return
            
            
            subsets.append(candidates[i])
            dfs(i+1, add+candidates[i])
            subsets.pop()
            while i+1<length and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, add)
            
        dfs(0, 0)
        return res