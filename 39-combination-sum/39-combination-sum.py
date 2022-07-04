class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """first of all we'll make a dfs through each candidate, 
        from next candidate onwards we won't take the candidate that we have already taken into               account and we'll dfs through that candidate"""
        
        def dfs(tmp, start, end, remains):
            if not remains:
                ans.append(tmp[:])
            elif remains>0:
                for idx in range(start, end):
                    tmp.append(candidates[idx])
                    dfs(tmp, idx, end, remains-candidates[idx])
                    tmp.pop()
        
        ans = []
        dfs([], 0, len(candidates), target)
        
        return ans
                
            
            
            