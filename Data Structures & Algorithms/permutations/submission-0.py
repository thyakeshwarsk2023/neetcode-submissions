class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        p = []
        used = set()

        def dfs():
            if len(p) == len(nums):
                res.append(p[:])
                return

            for num in nums:
                if num in used:
                    continue

                p.append(num)
                used.add(num)
                dfs()

                p.pop()
                used.remove(num)
        dfs()

        return res                
        