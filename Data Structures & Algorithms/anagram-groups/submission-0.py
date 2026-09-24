from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            ana_map[sorted_str].append(s)

        return list(ana_map.values())