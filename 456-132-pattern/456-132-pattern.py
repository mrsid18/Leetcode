class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        q=deque([])
        prevmin = -inf
        
        for i in range(len(nums)-1, -1, -1):
            
            while q and nums[i]>q[-1]:
                prevmin = q.pop()
            
            q.append(nums[i])
            if len(q)>=2 and prevmin>nums[i]: return True
                
        
        return False
                