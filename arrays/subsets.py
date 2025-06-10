# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution(object):
    def subsets(self, nums):

        # use BACKTRACK heper function algorithim --> recursion

        result = []

        def backtrack(start, path):
            result.append(path[:])      # creates copy of current subset
            for i in range(start, len(nums)):
                path.append(nums[i])        # adds curr num to curr subset 
                backtrack(i + 1, path)  # calls backtrack fxn recursively to include next num
                path.pop() # backtrack --- > excludes current num from subset

        backtrack(0, [])
        return result
        

    # https://www.youtube.com/watch?v=RtpJOGvfo7E
  # above is a link to a video I used to help me grasp the backtrack algorithm 
