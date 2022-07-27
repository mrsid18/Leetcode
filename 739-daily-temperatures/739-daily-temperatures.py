class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        
        q = deque([])
        
        for i in range(len(temperatures)):
            
            while q and temperatures[i]>temperatures[q[-1]]:
                tmp = q.pop()
                res[tmp] = i - tmp
            
            q.append(i)
        
        return res