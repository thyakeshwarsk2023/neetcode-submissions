class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k = sum(nums)
        if k % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = {0}

        for num in nums:
            next_dp = set()
            for s in dp:
                if s + num == target:
                    return True

                next_dp.add(s)
                next_dp.add(s+num)
            dp = next_dp        
        
        return target in dp