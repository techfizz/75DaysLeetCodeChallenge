class Solution:
    def rob(self, nums: List[int]) -> int:
        dp: list[int] = [-1] * (len(nums)+1)
        return self.helper(0, nums, dp)

    def helper(self, i: int, nums: list[int], dp: list[int]) -> int:
        if i >= len(nums):
            return 0

        if dp[i] != -1:
            return dp[i]

        steal: int = nums[i] + self.helper(i+2, nums, dp)
        skip: int = self.helper(i+1, nums, dp)

        dp[i] = max(steal,  skip)
        return dp[i]
        