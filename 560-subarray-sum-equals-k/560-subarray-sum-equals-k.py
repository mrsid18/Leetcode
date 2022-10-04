class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        
        hmap = {0:1}
        
        res = 0
        
        for num in nums:
            prefix+=num
            
            if prefix-k in hmap:
                res+=hmap[prefix-k]
                
            hmap[prefix] = hmap.get(prefix, 0) + 1
            
        return res