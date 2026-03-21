class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0  # position for next non-zero
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
                # fill the rest with zeros
        for i in range(k, len(nums)):
            nums[i] = 0


        