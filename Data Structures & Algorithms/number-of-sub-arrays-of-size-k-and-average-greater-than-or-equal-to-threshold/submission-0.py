class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k*threshold
        count  = 0

        curr_sum = sum(arr[:k])
        if curr_sum >= target_sum:
            count += 1

        for i in range(k,len(arr)):
            curr_sum += arr[i] - arr[i-k]
            if curr_sum >= target_sum:
                count+= 1

        return count            

