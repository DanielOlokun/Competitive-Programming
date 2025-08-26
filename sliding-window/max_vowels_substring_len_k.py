Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

class Solution(object):
    def maxVowels(self, s, k):

        # k = the length the substring has to be
        # get the substring that has most vowels in it

        # count starts off at whatever amount of vowels in s[:k]
        # if next one is vowel + 1, remove the very first one
        # if > curr_max .: max

        vowels = 'aeiou'

        curr_vowels = max_vowels = sum(1 for char in s[:k] if char in vowels)

        for i in range(k, len(s)):

          # sliding the window -- > ie, removing first char
            if s[i - k] in vowels:
                curr_vowels -= 1

          # adding last one -- > acts as a slide
            if s[i] in vowels:
                curr_vowels += 1

          # compare curr and max and make change if necessary
            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels
