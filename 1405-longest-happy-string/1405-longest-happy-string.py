class Solution:
    def longestDiverseString(self, A: int, B: int, C: int) -> str:
#         A>B>C
        a, b, c = 'a', 'b', 'c'
        if C>B:
            B, C = C, B
            b, c = c, b
        if B>A: 
            A, B = B, A
            a, b = b, a
        if C>B:
            B, C = C, B
            b, c = c, b

        res = ""
        while A and B:
            res += a
            A-=1
            if A>B:
                res +=a
                A-=1
            if B:
                res +=b
                B-=1
            if C>B:
                B, C = C, B
                b, c = c, b
            if B>A: 
                A, B = B, A
                a, b = b, a
            if C>B:
                B, C = C, B
                b, c = c, b
        
        if A:
            n = min(A,2)
            res += (a+a) if n==2 else a
        
        return res