# Time: log(min(n, m))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        totalLen = len(nums1)+len(nums2)
        half = totalLen//2
        
        if len(nums2)<len(nums1):
            A, B = B, A
        
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            Aleft = A[i] if i>=0 else -inf
            Aright = A[i+1] if i+1<len(A) else inf
            Bleft = B[j] if j>=0 else -inf
            Bright = B[j+1] if j+1<len(B) else inf
            
            if Aleft<=Bright and Bleft<=Aright:
                if totalLen%2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Aright, Bright))/2
            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1
            
            