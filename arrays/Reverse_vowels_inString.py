class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s_list = list(s)

        left, right = 0, len(s_list) - 1      #NB**

        while left < right:          #NB***
            if s_list[left] not in vowels:
                left+= 1
            elif s_list[right] not in vowels:
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1


        return ''.join(s_list)

        # this swaps whats in s and puts it into s_list


# left, right pointer algorithm 
