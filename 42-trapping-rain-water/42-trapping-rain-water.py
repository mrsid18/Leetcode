class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxL, maxR = 0,0
        area = 0
        i=0
        while l<r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            
            curArea = min(maxL, maxR) - height[i]
            if curArea>0: area+=curArea
            
            if maxL<maxR:
                l+=1
                i=l
            else:
                r-=1
                i=r
            
        return area
            
            