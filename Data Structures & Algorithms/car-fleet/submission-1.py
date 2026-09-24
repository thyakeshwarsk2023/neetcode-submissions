class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        fleets = 0
        current_maxtime = 0.0

        for p,s in cars:
            time = (target - p)/s

            if time > current_maxtime:
                fleets += 1
                current_maxtime = time

        return fleets
                