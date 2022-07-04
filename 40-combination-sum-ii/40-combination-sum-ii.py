class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(tmp, start, end, remains):
            if remains==0:
                ans.append(tmp[:])
            elif remains>0:
                for i in range(start, end):
                    if i>start and candidates[i]==candidates[i-1]: continue
                    tmp.append(candidates[i])
                    dfs(tmp, i+1, end, remains-candidates[i])
                    tmp.pop()
                
        ans = []
        candidates.sort()
        dfs([], 0, len(candidates), target)
        return ans