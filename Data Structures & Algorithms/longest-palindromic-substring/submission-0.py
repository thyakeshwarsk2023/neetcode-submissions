class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        def expand(l,r):
            nonlocal start, max_len

            while(
                l>=0
                and r < len(s)
                and s[l] == s[r]
            ):
               curr_len = r - l +1 
               if curr_len > max_len:
                max_len = curr_len
                start = l
               l -= 1
               r += 1

        for i  in range(len(s)):
            expand(i,i)
            expand(i,i+1)

        return s[start : start +max_len]        



        