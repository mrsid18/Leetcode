class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p=1
        
        for num in nums:
            output.append(p)
            p*=num
        
        p=1
        
        for idx,num in enumerate(nums[::-1]):
            output[-1-idx] *= p
            p*=num
            
        return output
      
        
        
            