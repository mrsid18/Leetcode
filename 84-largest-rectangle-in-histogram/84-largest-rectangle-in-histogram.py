class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        
        q = deque([])
        res = [0]*len(heights)
        
        for i in range(len(heights)):
            while q and heights[i]<heights[q[-1]]:
                j = q.pop()
                res[j] += heights[j]*(i-j)
            q.append(i)
        
        q = deque([])
        for i in range(len(heights)-2, -2, -1):
            while q and heights[i]<heights[q[-1]]:
                j = q.pop()
                res[j] += heights[j]*(j-i-1)
            q.append(i)
            
        return max(res)