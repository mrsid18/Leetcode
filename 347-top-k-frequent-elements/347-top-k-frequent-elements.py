class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
        
        f = [[] for _ in range(len(nums)+1)]
        
        for n,freq in hmap.items():
            f[freq].append(n)
        
        res = []
        i = len(f)-1
        print(f)
        while k:
            if f[i]:
                res.append(f[i].pop())
                k-=1
            else:
                i-=1
        
        return res
            
                
            
            