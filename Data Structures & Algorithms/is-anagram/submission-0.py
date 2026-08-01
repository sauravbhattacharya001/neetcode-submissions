class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s1= {}
        t1= {}

        for si, ti in zip(s,t):
            if si not in s1:
                s1[si] = 0
            s1[si] += 1

            if ti not in t1:
                t1[ti] = 0
            t1[ti] += 1


        for si in s1:
            if (si not in t1) or (s1[si] != t1[si]):
                return False

        return True            