class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dp = [0]*len(arr)
        stack = []
        for i in range(len(arr)):
            
            while stack and arr[i]<arr[stack[-1]]:
                stack.pop()
            
            j = stack[-1] if stack else -1
            
            dp[i] = dp[j] + (i-j)*arr[i]
            
            stack.append(i)
        
        return sum(dp)%(10**9+7)