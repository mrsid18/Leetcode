class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        minRes = [0]*len(nums)
        maxRes = [0]*len(nums)
        minStack = []
        maxStack = []
        
        for i in range(len(nums)):
            
            while maxStack and nums[i]<nums[maxStack[-1]]:
                maxStack.pop()
                
            while minStack and nums[i]>nums[minStack[-1]]:
                minStack.pop()
            
            j = maxStack[-1] if maxStack else -1
            k = minStack[-1] if minStack else -1
            
            maxRes[i] = maxRes[j] + nums[i]*(i-j)
            minRes[i] = minRes[k] + nums[i]*(i-k)
            
            maxStack.append(i)
            minStack.append(i)
            
        return sum(minRes)-sum(maxRes)