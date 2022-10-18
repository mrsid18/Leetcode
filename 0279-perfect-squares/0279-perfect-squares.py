"""
One way of thinking can be like 
1. Make an array of squares till n//2
1 -> 1
2->1+1
3->2+1
4->3+1, 4
5->4+1
6->dp[5]+1
8->dp[7]+dp[1], dp[4]+dp[4]
9->dp[4]+dp[5], 1
12->dp[11]+1, 4

"""



class Solution:
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        d, q, nq = 1, {n}, set()
        while q:
            for node in q:
                for square in squares:
                    if node == square: return d
                    if node < square: break
                    nq.add(node-square)
            q, nq, d = nq, set(), d+1
