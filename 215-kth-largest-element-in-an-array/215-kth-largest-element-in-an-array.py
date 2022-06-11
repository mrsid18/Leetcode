class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def qs(l,r):
            pivot, p = nums[r], l
            
            for i in range(l, r):
                if nums[i]<=pivot:
                    nums[i],nums[p] = nums[p], nums[i]
                    p+=1
            
            nums[r], nums[p] = nums[p], nums[r]
            
            if p>k: return qs(l, p-1)
            elif p<k: return qs(p+1, r)
            else: return nums[p]
        
        return qs(0, len(nums)-1)
                    
                    