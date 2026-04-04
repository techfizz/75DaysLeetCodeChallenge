class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target not in nums:
            for i in nums:
                if i>target:
                    pos=nums.index(i)
                    nums.insert(pos,target)
                    return nums.index(target)
                    
            else:
                nums.append(target)
                return nums.index(target)


