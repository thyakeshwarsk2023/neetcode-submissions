from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_map = {0:1}
        current_sum = 0
        for num in nums:
            current_sum += num
            diff = current_sum - k
            if diff in pre_map:
                count += pre_map[diff]

            pre_map[current_sum] = pre_map.get(current_sum,0) + 1

        return count    

