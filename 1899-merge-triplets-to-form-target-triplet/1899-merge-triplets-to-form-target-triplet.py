class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        a,b,c = target
        aP, bP, cP = False, False, False
        for x,y,z in triplets:
            if not (x>a or y>b or z>c): good.add((x,y,z))
        
        for x,y,z in good:
            if x==a: aP = True
            if y==b: bP = True
            if z==c: cP = True
        
        return aP and bP and cP