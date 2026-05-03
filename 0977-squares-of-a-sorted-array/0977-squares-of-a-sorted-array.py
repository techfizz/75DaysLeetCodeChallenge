class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        i,j=0,len(nums)-1
        while i<=j:
            a=nums[i]*nums[i]
            b=nums[j]*nums[j]
            if a>b:
                res.append(a)
                i+=1
            else:
                res.append(b)
                j-=1
        return res[::-1]
