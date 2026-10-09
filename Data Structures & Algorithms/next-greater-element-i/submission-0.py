class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsidx = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]

            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = numsidx[val]
                res[idx] = cur

            if cur in numsidx:
                stack.append(cur)

        return res            