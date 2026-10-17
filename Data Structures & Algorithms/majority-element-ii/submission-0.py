class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = 0
        count1 = count2 = 0

        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
            elif count1 == 0:
                c1 = num
                count1 = 1

            elif count2 == 0:
                c2 = num 
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for c in [c1,c2]:
            if c is not None and nums.count(c) > len(nums) // 3:
                if c not in result:
                    result.append(c)

        return result                          

                    
