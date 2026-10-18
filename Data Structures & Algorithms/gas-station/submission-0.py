class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]

            total_gas += net
            tank += net

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= 0  else -1        