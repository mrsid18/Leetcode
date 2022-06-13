class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        
        while l<r:
            h= min(height[l], height[r])
            res = max(res,h*(r-l))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        
        return res
                    