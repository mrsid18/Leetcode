class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = len(nums)//2
        index=0
        while len(nums)>0:
            if target==nums[middle]:
                return index+middle
            elif target>nums[middle]:
                index+=middle+1
                nums = nums[middle+1:]
            else:
                nums = nums[:middle]
             
            middle = len(nums)//2
        
        return -1
            