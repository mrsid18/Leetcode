class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        l = r = 0
        
        while r < len(nums):
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            
            q.append(r)
            
            if r+1-l == k:
                res.append(nums[q[0]])
                l+=1
                if q[0]<l: q.popleft()
            
            r+=1
        
        return res
        
        
        
            
        