class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, then sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_max_time = 0.0
        
        for p, s in cars:
            # Calculate time for current car to reach target
            time = (target - p) / s
            
            # If this car takes more time than the fleet in front,
            # it cannot catch up and thus forms a new fleet.
            if time > current_max_time:
                fleets += 1
                current_max_time = time
                
        return fleets