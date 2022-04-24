class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        
        for num in nums:
            if num in hashMap:
                hashMap[num] +=1
            else:
                hashMap[num] = 1            
            
        output = []
        
        for i in range(k):
            temp = max(hashMap, key=hashMap.get)
            output.append(temp)
            del hashMap[temp]
            
        return output