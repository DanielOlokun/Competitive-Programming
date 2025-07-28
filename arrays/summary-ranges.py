You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.


class Solution(object):
    def summaryRanges(self, nums):

        result = []
        if not nums:
            return result

        start = 0  # start of the current range

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    result.append(str(nums[start]))  # single number
                else:
                    result.append("{}->{}".format(nums[start], nums[i - 1]))
                start = i  # start a new range

    # Handle the last range
        if start == len(nums) - 1:
            result.append(str(nums[start]))
        else:
            result.append("{}->{}".format(nums[start], nums[-1]))

        return result
