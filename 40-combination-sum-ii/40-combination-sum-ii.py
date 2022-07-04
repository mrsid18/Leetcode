class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(tmp, start, end, remains):
            if remains==0:
                ans.append(tmp[:])
            elif remains>0:
                for idx in range(start, end):
                    if idx>start and candidates[idx]==candidates[idx-1]: 
                        continue
                    tmp.append(candidates[idx])
                    dfs(tmp, idx+1, end, remains - candidates[idx])
                    tmp.pop()
        
        ans = []
        candidates.sort(reverse=True)
        dfs([], 0, len(candidates), target)
        return ans