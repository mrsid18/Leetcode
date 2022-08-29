class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        q = []
        
        res = [0]*len(temperatures)
        
        for idx, temp in enumerate(temperatures):
            while q and temp>temperatures[q[-1]]:
                i = q.pop()
                res[i] = idx-i
            q.append(idx)
        
        return res