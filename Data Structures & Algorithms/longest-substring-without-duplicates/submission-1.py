class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right in  range(len(s)):
            curr_char = s[right]

            if curr_char in char_map and char_map[curr_char]>= left:
                left = char_map[curr_char] + 1

            char_map[curr_char] = right
            max_len = max(max_len , right - left + 1)

        return max_len        
        