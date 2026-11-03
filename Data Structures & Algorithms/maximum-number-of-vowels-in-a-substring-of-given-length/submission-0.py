class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        curr_vowel = 0

        for i in range(k):
            if s[i] in vowels:
                curr_vowel+= 1

        max_vowel = curr_vowel
        if max_vowel == k:
            return k


        for i in range(k,len(s)):
            if s[i] in vowels:
                curr_vowel += 1

            if s[i-k] in vowels:
                curr_vowel -= 1

            if curr_vowel >  max_vowel:
                max_vowel =curr_vowel
                if max_vowel == k:
                    return k

        return max_vowel            

