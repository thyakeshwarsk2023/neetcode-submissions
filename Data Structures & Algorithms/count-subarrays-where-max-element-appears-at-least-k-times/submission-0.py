class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val  = max(nums)
        count = 0
        ans = 0
        left = 0

        for right in range(len(nums)):

            if nums[right] == max_val:
                count += 1

            while count == k:
                if nums[left] == max_val:
                    count -= 1
                left += 1

            ans+=left


        return ans            
 

