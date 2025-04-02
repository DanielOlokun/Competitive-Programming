# The Question basically said -  In a given array, every element (int) appears twice but one. Find that one.
# I found this q interesting, due to the use of XOR (^=) usually used in Logic/ Discrete Maths.
#
#
#
# One to note

def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
