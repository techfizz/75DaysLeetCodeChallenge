class Solution:
    def reverseWords(self, s: str) -> str:
        l=[] 
        for i in s.split(): 
            l.append(i)
            w=" ".join(l[::-1])  
        return w
        
