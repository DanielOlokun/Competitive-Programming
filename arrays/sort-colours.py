# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


class Solution(object):
    def sortColors(self, nums):

        # COUNTING SORT ALGORITHIM ---- > a sorthing algorithim thatr counts frequency of nums in an array, then adds each number to array (sorted) based on its frequency
        
        count = [0] * 3  # Since only 0, 1, 2 exist  ---> As per Q

        for num in nums:
            count[num] += 1

        index = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[index] = color
                index += 1


