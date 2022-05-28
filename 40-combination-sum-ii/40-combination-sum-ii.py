class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        subsets = []
        candidates.sort()
        length = len(candidates)
        def dfs(i):
            if i==length or sum(subsets)>=target:
                if sum(subsets)==target: res.append(subsets[:])
                return
            
            
            subsets.append(candidates[i])
            dfs(i+1)
            subsets.pop()
            while i+1<length and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1)
            
        dfs(0)
        return res