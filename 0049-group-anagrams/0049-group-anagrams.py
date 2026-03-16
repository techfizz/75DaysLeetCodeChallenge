class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            e=' '.join(sorted(s))
            if e not in d:
                d[e]=[s]
            else:
                d[e]=d[e] +[s]
        return list(d.values())
        