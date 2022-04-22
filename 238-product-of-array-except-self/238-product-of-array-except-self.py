class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        if not 0 in nums:
            productOfAll = 1
            for num in nums:
                productOfAll*=num
                
            for num in nums:
                output.append(productOfAll//num)
            
            return output
        
        zeroIndices = [i for i, x in enumerate(nums) if x==0]
        
        output = [0]*len(nums)
        
        if len(zeroIndices) > 1:
            return output
        
        product = 1
        for num in nums:
            if num:
                product*=num
        
        output[zeroIndices[0]] = product
        
        return output
        
        
        
            