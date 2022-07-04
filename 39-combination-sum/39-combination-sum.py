class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(tmp, cur, end, remains):
            if cur==end: return
            if remains==0:
                ans.append(tmp[:])
            elif remains>0:
                tmp.append(candidates[cur])
                dfs(tmp, cur, end, remains-candidates[cur])
                tmp.pop()
                dfs(tmp, cur+1, end, remains)
        ans = []
        dfs([], 0, len(candidates), target)
        return ans
            