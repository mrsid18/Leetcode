class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
        
        f = list(hmap.values())
        f.sort(reverse=True)
        f=f[:k]
        
        res = []

        for n, freq in hmap.items():
            if freq in f:
                res.append(n)
        
        return res
                
            
            