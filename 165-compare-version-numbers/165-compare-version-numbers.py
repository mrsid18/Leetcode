class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        
        d = len(v1)-len(v2)
        v1 += [0]*-d
        v2 += [0]*d
        
        for i in range(len(v1)):
            if v1[i]<v2[i]: return -1
            if v1[i]>v2[i]: return 1
        
        return 0