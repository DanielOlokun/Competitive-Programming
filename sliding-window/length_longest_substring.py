Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.


  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        max_len = 0
        seen = set()

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            max_len = max(max_len, end - start + 1)

        return max_len  
