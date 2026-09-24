class Solution:
    def moveZeroes(self, nums: List[int]) -> N:
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
