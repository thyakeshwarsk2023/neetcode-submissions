from typing import List
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)

        for sandwhich in sandwiches:
            if counts[sandwhich] == 0:
                break

            counts[sandwhich] -= 1


        return counts[0] + counts[1]        

        