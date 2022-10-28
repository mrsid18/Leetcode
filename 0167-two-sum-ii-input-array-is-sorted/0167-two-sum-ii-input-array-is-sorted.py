class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l<=r:
            add = numbers[l]+numbers[r]
            if add==target: return l+1, r+1
            if add>target:
                r-=1
            else:
                l+=1
                while l and numbers[l]==numbers[l-1]:
                    l+=1