class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        y={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i] +1

        for r in t:
            if r not in y:
                y[r]=1
            else:
                y[r]=y[r] +1

        if d==y:
            return True
        else:
            return False