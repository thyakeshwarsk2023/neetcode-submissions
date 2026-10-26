class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        jumps = 0
        curr_end = 0

        for i in range(len(nums) - 1):

            far = max(far, i + nums[i])

            if i  == curr_end:
                jumps+= 1
                curr_end = far

        return jumps        
