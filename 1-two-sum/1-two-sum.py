class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for idx,num in enumerate(nums):
            res = target - num
            if res in hashMap:
                return [hashMap[res], idx]
            
            hashMap[num] = idx
            
            
        