class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        length = max(len(v1), len(v2))
        for i in range(length):
            if i >= len(v1):
                n1 = 0
            else:
                n1 = int(v1[i])
            if i >= len(v2):
                n2 = 0
            else:
                n2 = int(v2[i])
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0
