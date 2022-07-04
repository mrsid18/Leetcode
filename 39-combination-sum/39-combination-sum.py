class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(tmp, start, end, remains):
            if remains==0:
                ans.append(tmp[:])
            elif remains>0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    dfs(tmp, i, end, remains-candidates[i])
                    tmp.pop()
        
        ans = []
        dfs([], 0, len(candidates), target)
        return ans