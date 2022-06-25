class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
        
        
        
        dp = [False]*len(nums)
        dp[-1] = True
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(1,nums[i]+1):
                if dp[i+j]:
                    dp[i] = dp[i+j]
                    break
        return dp[0]
        