class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n^res
        
        return res
        
        
        # dicto = dict()
        # for num in nums:
        #     dicto[num] = dicto.get(num,0)+1
        #     if (dicto[num]) == 2:
        #         dicto.pop(num)
        # return list(dicto.keys())[0]
#         nums.sort()
#         result=0
#         while nums and len(nums)>1:
#             result=nums[0]
#             num1=nums[0]
#             num2=nums[1]
#             if num1 != num2:
#                 return result
#             nums = nums[2:]
        
#         return nums[0]

        