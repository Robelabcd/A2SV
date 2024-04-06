class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = list(map(int, v1.split('.'))); v2 = list(map(int, v2.split('.')));
        n1 = len(v1); n2 = len(v2);
        maxx = max(n1, n2); 
        v1 += [0]*(maxx - n1); v2 += [0]*(maxx - n2);
        for i in range(maxx):
            if v1[i] < v2[i]: return -1;
            if v1[i] > v2[i]: return 1;
        return 0