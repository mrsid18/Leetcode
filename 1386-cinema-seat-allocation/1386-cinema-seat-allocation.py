class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reserved = defaultdict(list)
        
        for row, col in reservedSeats:
            reserved[row].append(col)
        
        res = 2*(n-len(reserved.keys()))
        for i in reserved.keys():
            if not any(col in reserved[i] for col in range(2,6)):
                res+=1
                reserved[i].append(4)
            if not any(col in reserved[i] for col in range(4,8)):
                res+=1
                reserved[i].append(6)
            if not any(col in reserved[i] for col in range(6,10)):
                res+=1
                    
        return res