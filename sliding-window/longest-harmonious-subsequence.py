We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.



from collections import Counter    # a class that helps count items in a list 

class Solution(object):
    def findLHS(self, nums):

        # using a dict

        freq = Counter(nums)    # counter class
        max_len = 0

        for num in freq:
            if num + 1 in freq:    # for each num in freq (dict) , if that number  + 1 is in freq :
                max_len = max(max_len, freq[num] + freq[num + 1])    # check if frequency of thta number  + number + 1 is greater than max occurences/length  + update if needed 

        return max_len
