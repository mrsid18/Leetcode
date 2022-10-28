class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        print(nums)
        for i, num in enumerate(nums):
            if i and nums[i-1]==num: continue
            target = -num
            l, r = i+1, n-1
            while l<r:
                add = nums[l]+nums[r]
                if add==target:
                    res.append([-target, nums[l], nums[r]])
                    l+=1
                    while l and l<r and nums[l]==nums[l-1]:
                        l+=1
                    r-=1
                elif add>target:
                    r-=1
                else:
                    l+=1
                    while l and l<r and nums[l]==nums[l-1]:
                        l+=1
        
        return res
                
        