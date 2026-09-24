class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(start , remaining):
            if remaining == 0:
                result.append(curr.copy())
                return

            if remaining < 0:
                return

            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i, remaining - nums[i])
                curr.pop()

        backtrack(0,target)

        return result        

