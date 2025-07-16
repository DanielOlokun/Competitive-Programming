class Solution(object):
    def findMaxAverage(self, nums, k):

        curr_sum = max_sum = sum(nums[:k])    # inital windows -- > current sum starts off as max sum which is the sum of nums from start of array to k ( as per q )

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]    # this slides the window -- > adds the next number of and removes the first one -- > efficiently -- > O(1) time
            max_sum = max(max_sum, curr_sum)    # updates max if needed


        return max_sum / float(k)  # ensures floating point as per q



        # initialise
        # get whats needed
        # slide window
        # update 
        # continue
