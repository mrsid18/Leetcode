class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #strictly non-decreasing (increasing queue)
        heights.append(-1)
        
        stack = []
        
        res = [0]*len(heights)
        
        for idx, h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                minh = stack.pop()
                res[minh] = (idx-minh)*heights[minh]
            stack.append(idx)
        
        stack = []
        for idx in range(len(heights)-2, -2, -1):
            while stack and heights[idx]<heights[stack[-1]]:
                i = stack.pop()
                res[i] += (i-idx-1)*heights[i]
            stack.append(idx)
        return max(res)
        